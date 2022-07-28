import ipywidgets as widgets


def draw_interactive_scatter_plot_ipy(*args, legend=[], size=(12, 6), title='', xlabel='', ylabel=''):
    names = []
    checkbox_objects = []
    colors = ['g', 'r', 'b']
    for i in range(len(args)):
        if legend:
            checkbox_objects.append(widgets.Checkbox(value=False, description=legend[i]))
            names.append(legend[i])
        else:
            checkbox_objects.append(widgets.Checkbox(value=False, description=args[i][1].name))
            names.append(args[i][1].name)

    arg_dict = {names[i]: checkbox for i, checkbox in enumerate(checkbox_objects)}

    ui = widgets.HBox(children=checkbox_objects)

    def show_hide_plots(**kwargs):
        plt.figure(figsize=size, dpi=80)
        for i, key in enumerate(kwargs):
            if kwargs[key] is True:
                plt.scatter(args[i][0], args[i][1], color=colors[i], alpha=0.2, s=1)
        if title:
            plt.title(title)

        if xlabel:
            plt.xlabel(xlabel)

        if ylabel:
            plt.ylabel(ylabel)

        plt.legend(legend)
        plt.show()

    out = widgets.interactive_output(show_hide_plots, arg_dict)
    display(ui, out)
