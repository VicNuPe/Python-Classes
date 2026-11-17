from camera_kit import CameraKit


def show_rental(item: CameraKit) -> None:
    #Display our already-existing camera kit object.
    print(item.display())


def main() -> None:
    kit = CameraKit("Canon", "R6", "CAM-001", "Mirrorless", 45.0)
    show_rental(kit)
    print("First booking:", kit.book())
    print("Second booking:", kit.book())
    print("Booked now:", kit.is_booked())
    kit.return_item()
    print("Booked after return:", kit.is_booked())
    kit.change_rate(49.50)
    print("New daily rate:", f"€{kit.check_rate():.2f}")


if __name__ == "__main__":
    main()
