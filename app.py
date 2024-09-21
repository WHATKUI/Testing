from flask import Flask, render_template
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

app = Flask(__name__)

# Buat figure dan axis
fig, ax = plt.subplots()

# Inisialisasi lingkaran
circle, = ax.plot([], [], 'o')

# Set batas axis
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Inisialisasi animasi
def init():
    circle.set_data([], [])
    return circle,

# Fungsi animasi
def animate(i):
    x = np.sin(i)
    y = np.cos(i)
    circle.set_data(x, y)
    return circle,

# Buat animasi
ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, blit=True)

# Render animasi sebagai template HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
