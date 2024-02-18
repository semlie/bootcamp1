# ::: Data Science Garage :::

import spacy
import spacy_setfit

# Create some example data
train_dataset = {
    'inlier': [
        'This text is about chairs',
        'Couches, benches and television',
        'I really need to get new sofa'
    ],
    'outlier': [
        'Text about kitchen equipment',
        'This text is about politics',
        'Comments about AI and stuff'
    ]
}

# Load the Spacy language model
nlp = spacy.load('en_core_web_sm')

# Add the text_categorizer pipeline component to the Spacy model,
# and configure it with Setfit parameter
nlp.add_pipe('text_categorizer', config={
    'pretrained_model_name_or_path': 'paraphrase-MiniLM-L3-v2',
    'setfit_trainer_args': {
        'train_dataset': train_dataset
    }
})

doc = nlp('I want to be strong politic')
print(f'{doc} = \n{doc.cats}')

# - - - - - - - - - - - - - - - - - -- - - - - - - - - - - -- - - - - -
# Want to change your carrer and become advances data scientist or
# data analytic? Check HERE! - https://turingcollege.org/DataScienceGarage