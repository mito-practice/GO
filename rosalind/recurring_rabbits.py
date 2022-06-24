
def rabbit(num_months, num_offspring):
    if num_months == 1:
        return 1
    if num_months == 2:
        return num_offspring
    first_gen = rabbit(num_months-1, num_offspring)
    second_gen = rabbit(num_months-2, num_offspring)
    if num_months <= 4:
        return first_gen + second_gen
    return first_gen + (second_gen*num_offspring)

print(rabbit(30, 2))


