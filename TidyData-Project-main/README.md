# Tidy Data Project: 2008 Olympic Medalists
By Jada Bautista

## The Project
This project applies the principles of **tidy data** to clean and explore a dataset of medalists from the 2008 Olympic Games. With the help of Python and data visualization methods, I transformed the set to produce a better display of sport popularity and gender representation.

I used the **Tidy Data** framework of Hadley Wickham to achieve this. Like in his paper, each variable is in its own column, each observation is in its own row, and each type of observational unit forms its own table

## The Dataset!
This dataset includes 2008 Olympic medalists with columns for each sport-gender combination wherein each of these values indicate the type of medal won.

### Source
This dataset is sourced from a structured version of Olympic records (2008) provided in my Elements of Computing II class.

### Preprocessing Steps
- Removed rows with all NaN sport entries
- Used `melt()` to reshape from wide to long format
- Split combined column (`event`) using `str.split()` to extract gender and sport
- Used `str.replace()` and `str.title()` to clean sport names
- Handled rare sports by grouping them under `"Other"`
- Applied encoding for analysis: Label Encoding and One-Hot Encoding

## Visualizations
2. **Bar Chart**: Medals won by gender
3. **Grouped Bar Chart**: Gender distribution across sports
4. **Lollipop Chart**: Top 10 sports with the most medals  

## Pivot Table
Summarized medal counts by sport and gender

## How to Run This Notebook

1. **Clone the repository**
git clone https://github.com/jadabau/TidyData-Project.git cd TidyData-Project

2. **Install the required dependencies**
- `pandas`
- `matplotlib`
- `seaborn`
- `LabelEncoder`

3. **Launch the notebook**
jupyter notebook Bautista_Tidy Data Project.ipynb

---

## References

- [**Tidy Data** by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)  
- [**Pandas Cheat Sheet**](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)  
