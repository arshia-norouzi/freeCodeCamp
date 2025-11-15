# run_sea_level.py

from sea_level_predictor import draw_plot

def main():
    # Produce and display the sea level projection figure
    axes = draw_plot()
    print("Sea level plot created successfully.")

if __name__ == "__main__":
    main()
