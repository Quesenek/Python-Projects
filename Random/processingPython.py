import processing_py as pp

def setup():
    size(100, 100, P3D)
    background(0)
    noStroke()
    directionalLight(51, 102, 126, -1, 0, 0)
    translate(20, 50, 0)
    sphere(30)

    