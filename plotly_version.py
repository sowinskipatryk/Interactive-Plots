import plotly.graph_objects as go


def draw_interactive_scatter_plotly(*args, names=[], title=''):
    fig = go.Figure()
    i = 0

    for arg in args:
        ax = arg[0]
        ay = arg[1]

        if len(ax.shape) != 1:
            ax = ax.reshape(-1)
        if len(ay.shape) != 1:
            ay = ay.reshape(-1)

        if names:
            fig.add_trace(go.Scatter(x=ax, y=ay, mode='markers', name=names[i]))
            i += 1
        else:
            fig.add_trace(go.Scatter(x=ax, y=ay, mode='markers'))

        if title:
            fig.update_layout(title={
                'text': title,
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

    fig.show()
