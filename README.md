# 1. Intro
This is my first attempt to build a webapp in Python, hence, Webapp One. The goal is to get familiar with Python and selected libraries and utilize as much of its functionalty as possible.

Webapp One is a data manipulation and visualization tool with interactive controls that lets users make changes and see the results on the fly.

Webapp One consists of two sections: *settings bar* for selecting date, time horizon and *output area* for displaying charts and tables.

This is by no means finished project and will be improved in future.

# 2. Required libraries
Following libraries are required for Webapp One to run smoothly and without hiccups:

* *Pandas* for data manipulation and recoding variables;

* *Plotly Express* for interactive charts;

* *Streamlit* as web framework;

* *datetime* for working with dates;


# 3. The data
There are 12 randomly generated .csv files, all located in the 'data' folder, serving as source for the Webapp One. Each file has 5 columns:

* *ID* - unique field indentifying the loan contract number.

* *Amount* - representing principal amount outstanding.

* *Principal* and *Interest overdue* - number of days passed due for principal payment and Interest overdue - number of days passed due for interest overdue days.

* *Loan type* - categorical variable for six loan types (i.e. 1 for mortgage loans, 2 for consumer loans etc.)


# 5. How to use the Webapp One
* User selects any *date* from the calendar marked as Date (user can select any day from year 2021) and *time horizon* using the slider, which indicates time series of what length should be displayed. *Note: User selects end date and number of month further back into the past.*

* Below the silder is the multiselect bar, where user can select one or multiple products to be displayed on chart (multiselect bar do not affect the expander boxes, those are always displayed).

# 6a. Visual Demo

https://user-images.githubusercontent.com/26896606/133501507-85ff43ec-21f4-49c2-bcbf-8a836a012e7f.mp4


# 6b. Web Version

https://share.streamlit.io/ashotm/webappone/main/application.py 

# 7. Future updates
There are some things, both functionality and appearance wise, that I am looking forward to adding to the Webapp One. First of all, I'd like to make a two page layout using radio button (since tabs are not available in Streamlit v0.87.0) for more diverse analysis (by product, by branch etc). Second, I'd like to improve on the overall appearance of the app: eliminate empty space and make charts visually appealing. Third, the speed. The app uses small .csv files, but with larger ones there will be speed issue.
