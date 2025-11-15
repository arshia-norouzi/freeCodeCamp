# run_medical_plots.py

import matplotlib.pyplot as plt
import medical_data_visualizer as viz

if __name__ == "__main__":
    # Generate the categorical plot
    cat_plot_figure = viz.draw_cat_plot()

    # Generate the correlation heatmap
    heatmap_figure = viz.draw_heat_map()

    # Display both figures
    plt.show()
