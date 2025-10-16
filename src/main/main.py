from src.main import snowflake, sierpinsky, fractal_plant


def main():
    #snowflake.draw_flake(3)

    rules = {
        "A": "B-A-B",
        "B": "A+B+A"
    }
    start = "A"
    angle = 60
    iterations = 10
    length = 3

    #sierpinsky.draw_curve(rules, start, angle, iterations, length)

    fractal_plant.start()

if __name__ == "__main__":
    main()
