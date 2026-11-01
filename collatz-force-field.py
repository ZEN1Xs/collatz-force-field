import numpy as np


def simulate_collatz_energy(start_number):
    x = start_number
    trajectory = [x]
    log_forces = []
    chaos_energy = []

    print(f"=== ЗАПУСК СИМУЛЯЦИИ ПОЛЯ СИЛ ДЛЯ X = {start_number} ===")
    print(
        f"{'Шаг':<5} | {'Число (x)':<12} | {'Импульс Силы (ln)':<20} | {'Энергия Хаоса':<15}"
    )
    print("-" * 60)

    step = 0
    while x > 1:
        current_energy = np.log(x)
        chaos_energy.append(current_energy)

        if x % 2 == 0:
            next_x = x // 2
            force = np.log(0.5)
        else:
            next_x = 3 * x + 1
            force = np.log((3 * x + 1) / x)

        log_forces.append(force)

        print(f"{step:<5} | {x:<12} | {force:<20.4f} | {current_energy:<15.4f}")

        x = next_x
        step += 1

        if step > 2000:
            print("Предохранитель: превышен лимит шагов!")
            break

    print(f"{step:<5} | {1:<12} | {0.0000:<20.4f} | {0.0000:<15.4f}")
    print("-" * 60)
    print("СИМУЛЯЦИЯ ЗАВЕРШЕНА: Система затухла в Центральный Ноль (цикл 4-2-1).")

    total_potential = sum(log_forces)
    avg_force = np.mean(log_forces)

    print(f"Суммарный баланс сил (Потенциал Ляпунова): {total_potential:.4f}")
    print(
        f"Средний импульс поля на шаг: {avg_force:.4f} (Отрицательный знак = гарантированное трение)"
    )


simulate_collatz_energy(27)
