from camera_kit import CameraKit

canon = CameraKit("Canon", "EOS R8", 230.33)
nikon = CameraKit("Nikon", "Z6 III", 250.00)
sony = CameraKit("Sony", "Alpha 7 III", 1950.00)

print("===== Camera Kit Rental =====")
print("1. Canon EOS R8")
print("2. Nikon Z6 III")
print("3. Sony Alpha 7 III")

choice = input("Pick a kit (1 to 3): ")

if choice == "1":
    canon.book()
    canon.display()
elif choice == "2":
    nikon.book()
    nikon.display()
elif choice == "3":
    sony.book()
    sony.display()
else:
    print("Invalid choice")
