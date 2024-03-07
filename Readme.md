# Room Inspection Checklist App

This Streamlit app allows users to conduct room inspections in a hotel or stay, using a checklist with a tick box for each item. The app also provides the functionality to add new rooms to the checklist.

## Features

* Select a room number from the dropdown menu to inspect the room.
* Tick the checkboxes for each item on the inspection checklist.
* Add new rooms to the checklist using the sidebar option.

## Prerequisites

Before running the app, make sure you have the following installed:

* Python 3.x
* Streamlit
* Pandas

You can install Streamlit and Pandas using pip:

```
pip install streamlit pandas
```

Run the Streamlit app:

```
streamlit run app.py

```


The app will open in your default web browser. You can select a room number from the dropdown menu and tick the checkboxes to perform an inspection.

## File Structure

* `app.py`: Main Streamlit application file.
* `room_inspection.xlsx`: Excel file containing the room inspection checklist data.(Will create by itself while running)
* `README.md`: Instructions and information about the app.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.
