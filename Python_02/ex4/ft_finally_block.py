#!/usr/bin/env python3

class PlantError(Exception):
    """Custom plant error."""
    def __init__(self, msg="Unknown plant error"):
        super().__init__(msg)


def water_plant(plant_list: list) -> None:
    """
    We verify that the list of plants provided is valid
    by checking whether they are included in the plant list.
    """
    plant = ["Tomato", "Letuce", "Carrots"]

    print("Opening watering system")
    try:
        for veg in plant_list:
            if veg not in plant:
                raise PlantError(f"Invalid plant name to water: '{veg}'\n"
                                 ".. ending tests and returning to main")
            if veg != veg.capitalize():
                raise PlantError(
                    f"Invalid plant name to water: '{veg}'\n"
                    ".. ending tests and returning to main"
                )
            else:
                print(f"Watering {veg}: [OK]")

    except PlantError as error:
        print(f"Caught PlantError: {error}")

    finally:
        print("Closing waterinf system (cleanup)")


def test_watering_system() -> None:
    """We test with a correct list and an incorrect one."""
    print("=== Garden Watering System ===\n")

    good_list = ["Tomato", "Letuce", "Carrots"]
    bad_list = ["Tomato", "letuce", "carrots"]

    print("Testing normal watering . . .")
    water_plant(good_list)

    print("\nTesting invalid plants . . .")
    water_plant(bad_list)

    print("\nCleanup always happens, even with errors!")
