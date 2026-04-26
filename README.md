# ⭐ If you find this useful, feel free to star the repo

# Trichology Terms

A glossary dataset of trichological, dermatological, cosmetic science, hair transplantation, nutrition, genetics, and research terms.


## Dataset

- `data/trichology_terms.csv`
- `data/trichology_terms.json`

Rows: **412**

## Python usage

```python
from trichology_terms import load_terms, search_terms, get_definition, list_categories

df = load_terms()
print(df.head())

print(get_definition("Alopecia"))
print(search_terms("scalp"))
print(list_categories())
```

## Columns

- `term_id`
- `term`
- `definition`
- `category`

## Install directly from GitHub

```bash
pip install git+https://github.com/YOUR-USERNAME/Trichology_Glossary_Terms.git


# The glossary dataset is provided for educational and research use. Definitions are based on personal learning notes and should not be treated as clinical advice.
