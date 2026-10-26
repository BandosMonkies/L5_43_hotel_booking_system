"""Hotel room reservation and booking management module."""

from __future__ import annotations

import hashlib
import secrets
from pathlib import Path
from typing import Optional


Room = dict[str, object]
BookingLog = list[str]

ROOM_INVENTORY: dict[str, Room] = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(
    room_num: str, guest_name: str, booking_log: Optional[BookingLog] = None
) -> bool:
    """Reserve an available room and record the reservation."""
    if room_num not in ROOM_INVENTORY or ROOM_INVENTORY[room_num]["is_booked"]:
        return False

    ROOM_INVENTORY[room_num]["is_booked"] = True
    if booking_log is None:
        booking_log = []
    booking_log.append(f"Reserved room {room_num} for guest {guest_name}")
    return True


def cancel_booking(room_num: str) -> bool:
    """Release a booked room, returning whether the room exists."""
    room = ROOM_INVENTORY.get(room_num)
    if room is None:
        return False
    room["is_booked"] = False
    return True


def check_room_status(room_num: str) -> bool:
    """Return whether a known room is currently available."""
    room = ROOM_INVENTORY.get(room_num)
    return room is not None and not room["is_booked"]


def compute_seasonal_rate(room_num: str, surge_multiplier: float) -> float:
    """Apply a positive seasonal multiplier to a room's base price."""
    if surge_multiplier <= 0:
        raise ValueError("surge_multiplier must be positive")

    room = ROOM_INVENTORY.get(room_num)
    if room is None:
        raise KeyError(f"Unknown room: {room_num}")
    return float(room["price"]) * surge_multiplier


def generate_guest_hash(guest_id: str) -> str:
    """Return a modern cryptographic digest for a guest identifier."""
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref() -> int:
    """Return a cryptographically secure four-digit booking reference."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename: str = "hotel_ledger.txt") -> None:
    """Write the current room inventory to a ledger file."""
    ledger_path = Path(filename)
    ledger_path.write_text(str(ROOM_INVENTORY), encoding="utf-8")
    print(f"Hotel ledger exported to: {ledger_path}")


def main() -> None:
    """Run a small demonstration of the booking system."""
    booking_log: BookingLog = []
    book_room("101", "Emma Watson", booking_log)
    cancel_booking("102")
    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())
    export_room_ledger()
    print("Booking log:", booking_log)


if __name__ == "__main__":
    main()
