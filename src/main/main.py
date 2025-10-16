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
    length = 5

    sierpinsky.draw_curve(rules, start, angle, iterations, length)

if __name__ == "__main__":
    main()
