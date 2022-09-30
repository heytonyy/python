from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def board():
    tile_colors = ['blue', 'green']
    return render_template('board.html', rows=int(8), cols=int(8),tile_colors=tile_colors,color_index=int(0))

@app.route('/<rows>')
def board_rows(rows):
    tile_colors = ['blue', 'green']
    return render_template('board.html', rows=int(rows), cols=int(8),tile_colors=tile_colors,color_index=int(0))

@app.route('/<rows>/<cols>')
def board_rows_cols(rows,cols):
    tile_colors = ['blue', 'green']
    return render_template('board.html', rows=int(rows), cols=int(cols),tile_colors=tile_colors,color_index=int(0))

@app.route('/<rows>/<cols>/<color1>')
def board_rows_cols_color1(rows,cols,color1):
    tile_colors = [color1, 'green']
    return render_template('board.html', rows=int(rows), cols=int(cols),tile_colors=tile_colors,color_index=int(0))

@app.route('/<rows>/<cols>/<color1>/<color2>')
def board_rows_cols_color1_color2(rows,cols,color1,color2):
    tile_colors = [color1, color2]
    return render_template('board.html', rows=int(rows), cols=int(cols),tile_colors=tile_colors,color_index=int(0))

if __name__ == '__main__':
    app.run(debug=True)
