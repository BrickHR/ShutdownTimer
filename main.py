import time
import os
import sys
import platform
import threading


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown /s /t 1')
    else:
        os.system('shutdown now')


def abort_shutdown():
    if platform.system() == "Windows":
        os.system('shutdown /a')
    clear_screen()
    print("\n    ❌ Timer abgebrochen! System bleibt an.")
    sys.exit()


def display_timer(seconds):
    total_seconds = seconds

    while seconds:
        try:
            clear_screen()
            minutes, secs = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)

            print(f"""
    ╔══════════════════════════╗
    ║     SHUTDOWN TIMER       ║
    ╠══════════════════════════╣
    ║  {hours:02d}:{minutes:02d}:{secs:02d} verbleibend  ║
    ╚══════════════════════════╝

    Drücke STRG+C zum Abbrechen
    """)

            progress_percent = (total_seconds - seconds) / total_seconds
            bar_length = 50
            filled_length = int(bar_length * progress_percent)
            progress = '█' * filled_length + '░' * (bar_length - filled_length)
            print(f"    [{progress}]")

            if seconds <= 10:
                print(f"\n    🚨 WARNUNG: Shutdown in {seconds} Sekunden! 🚨")
            elif seconds <= 30:
                print(f"\n    ⚠️  Hinweis: Weniger als 30 Sekunden verbleibend!")
            elif seconds <= 60:
                print(f"\n    ℹ️  Info: Weniger als 1 Minute verbleibend")

            time.sleep(1)
            seconds -= 1

        except KeyboardInterrupt:
            abort_shutdown()

    clear_screen()
    print("\n    💤 System fährt herunter... Auf Wiedersehen! 👋\n")
    time.sleep(2)
    shutdown()


def main():
    try:
        while True:
            clear_screen()
            print("""
    🕒 Shutdown-Timer 🕒

    1. Timer in Minuten
    2. Timer in Stunden
    3. Timer zu bestimmter Uhrzeit
    4. Beenden
    """)
            choice = input("    Wähle eine Option (1-4): ")

            if choice == "1":
                minutes = int(input("\n    Wie viele Minuten bis zum Shutdown? "))
                if minutes < 0:
                    print("\n    Bitte geben Sie eine positive Zahl ein!")
                    time.sleep(2)
                    continue
                seconds = minutes * 60

            elif choice == "2":
                hours = int(input("\n    Wie viele Stunden bis zum Shutdown? "))
                if hours < 0:
                    print("\n    Bitte geben Sie eine positive Zahl ein!")
                    time.sleep(2)
                    continue
                seconds = hours * 3600

            elif choice == "3":
                target_time = input("\n    Zu welcher Uhrzeit soll der PC herunterfahren? (Format: HH:MM) ")
                try:
                    target_hour, target_minute = map(int, target_time.split(':'))
                    current_time = time.localtime()
                    current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60
                    target_seconds = target_hour * 3600 + target_minute * 60

                    if target_seconds <= current_seconds:
                        target_seconds += 24 * 3600

                    seconds = target_seconds - current_seconds
                except:
                    print("\n    ⚠️ Ungültiges Zeitformat! Bitte HH:MM verwenden.")
                    time.sleep(2)
                    continue

            elif choice == "4":
                print("\n    Programm wird beendet...")
                time.sleep(1)
                sys.exit()

            else:
                print("\n    ⚠️ Ungültige Eingabe!")
                time.sleep(2)
                continue

            print(f"\n    Timer wird gestartet...")
            time.sleep(2)
            display_timer(seconds)

    except KeyboardInterrupt:
        abort_shutdown()
    except ValueError:
        print("\n    ⚠️ Bitte geben Sie eine gültige Zahl ein!")
        time.sleep(2)


if __name__ == "__main__":
    main()