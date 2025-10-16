from src.main import snowflake, sierpinsky


def main():
    #snowflake.draw_flake(3)

    rules = {
        "A": "B-A-B",
        "B": "A+B+A"
    }
    start = "A"
    angle = 60
    iterations = 10
    length = 10

    sierpinsky.draw_curve(start, angle, length, iterations)

if __name__ == "__main__":
    main()
