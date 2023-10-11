from fastai.text.all import *
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import paths

if __name__ == "__main__":
    # Finetune language model using sentiment data
    dls_lm = DataBlock(
        blocks=TextBlock.from_folder(paths.TEXT, is_lm=True),
        get_items=get_text_files,
        splitter=RandomSplitter(0.1),
    ).dataloaders(paths.TEXT, path=paths.TEXT, bs=128, seq_len=80)

    learn = language_model_learner(
        dls_lm, AWD_LSTM, drop_mult=0.3,
        metrics=[accuracy, Perplexity()]).to_fp16()
    learn.fit_one_cycle(1, 2e-2)
    learn.save_encoder('finetuned')

    # Train a classifier using the finetuned language model
    dls_clas = DataBlock(
        blocks=(TextBlock.from_folder(paths.TEXT, vocab=dls_lm.vocab), CategoryBlock),
        get_y=parent_label,
        get_items=get_text_files,
        splitter=RandomSplitter(0.1),
    ).dataloaders(paths.TEXT, path=paths.TEXT, bs=128, seq_len=72)

    learn2 = text_classifier_learner(dls_clas, AWD_LSTM, drop_mult=0.5,
                                    metrics=accuracy).to_fp16()
    learn2 = learn2.load_encoder('finetuned')
    learn2.fit_one_cycle(1, 2e-2)

    # Try a few predictions
    print(learn2.predict("happy great fun"))
    print(learn2.predict("sad bad mad"))
    print(learn2.predict("inferior gross garbage"))
    print(learn2.predict("superlative nice friendly"))
