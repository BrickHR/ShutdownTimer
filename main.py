import time
import os
import sys
import platform


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown /s /t 1')
    else:
        os.system('shutdown now')


def display_timer(seconds):
    total_seconds = seconds  # Speichern der Gesamtzeit für die Fortschrittsberechnung
    while seconds:
        clear_screen()
        minutes, secs = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        print(f"""
    ╔══════════════════════════╗
    ║     SHUTDOWN TIMER       ║
    ╠══════════════════════════╣
    ║  {hours:02d}:{minutes:02d}:{secs:02d} verbleibend  ║
    ╚══════════════════════════╝
    """)

        # Berechnung des Fortschritts in Prozent
        progress_percent = (total_seconds - seconds) / total_seconds
        bar_length = 50
        filled_length = int(bar_length * progress_percent)
        progress = '█' * filled_length + '░' * (bar_length - filled_length)
        print(f"    [{progress}]")

        if seconds <= 10:
            print(f"\n    ⚠️  WARNUNG: Shutdown in {seconds} Sekunden! ⚠️")

        time.sleep(1)
        seconds -= 1

    clear_screen()
    print("\n    💤 System fährt herunter... Auf Wiedersehen! 👋\n")
    time.sleep(2)
    shutdown()


def main():
    try:
        clear_screen()
        print("\n    🕒 Shutdown-Timer 🕒")
        minutes = int(input("\n    Wie viele Minuten bis zum Shutdown? "))

        if minutes < 0:
            print("\n    Bitte geben Sie eine positive Zahl ein!")
            return

        seconds = minutes * 60
        print(f"\n    Timer für {minutes} Minuten wird gestartet...")
        time.sleep(2)
        display_timer(seconds)

    except KeyboardInterrupt:
        clear_screen()
        print("\n    ❌ Timer abgebrochen! System bleibt an.")
        sys.exit()
    except ValueError:
        print("\n    ⚠️ Bitte geben Sie eine gültige Zahl ein!")


if __name__ == "__main__":
    main()