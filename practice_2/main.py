# main.py
from data_processing import process_data


def main() -> None:
    print("=== Демонстрация работы пакета data_processing ===")

    raw = [10, None, -5, 3.5, "7", 0, 12.3, -1]

    print("Исходные данные:", raw)

    result = process_data(raw)

    print("\nОчищенные данные:")
    print(result["cleaned_values"])

    print("\nСтатистики:")
    for key, value in result["stats"].items():
        print(f"{key}: {value}")

    print("\nОтчет:")
    print(result["report"])

    print("\nВизуализация:")
    print(result["histogram"])


if __name__ == "__main__":
    main()
