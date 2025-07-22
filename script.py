#1

real_value = 100.00
dollar_rate = 5.20
euro_rate = 6.15

dollar_value = real_value / dollar_rate
rounded_dollar_value = round(dollar_value, 2)

euro_value = real_value / euro_rate
rounded_euro_value = round(euro_value, 2)

print(f"R$ {real_value:.2f} é equivalente a:")
print(f"US$ {rounded_dollar_value:.2f} (Dollar)")
print(f"€ {rounded_euro_value:.2f} (Euro)")

print("-------------------------------")

#2

product_name = "Camiseta"
original_price = 50.00
discount_percentage = 20

discount_amount = original_price * (discount_percentage / 100)

final_price = original_price - discount_amount

print(f"Produto: {product_name}")
print(f"Preço Original: R$ {original_price:.2f}")
print(f"Desconto: {discount_percentage}%")
print(f"Valor do Desconto: R$ {discount_amount:.2f}")
print(f"Preço Final: R$ {final_price:.2f}")

print("-------------------------------")

#3

grade1 = 7.5
grade2 = 8.0
grade3 = 6.5

average_grade = (grade1 + grade2 + grade3) / 3

rounded_average_grade = round(average_grade, 2)

print(f"Notas do Aluno:")
print(f"Nota 1: {grade1:.1f}")
print(f"Nota 2: {grade2:.1f}")
print(f"Nota 3: {grade3:.1f}")
print(f"Média Final: {rounded_average_grade:.2f}")

print("-------------------------------")

#4

distance_km = 300
fuel_liters = 25

fuel_consumption_km_per_liter = distance_km / fuel_liters

rounded_fuel_consumption = round(fuel_consumption_km_per_liter, 2)

print(f"Detalhes da Viagem:")
print(f"Distância Percorrida: {distance_km} km")
print(f"Combustível Gasto: {fuel_liters} litros")
print(f"Consumo Médio: {rounded_fuel_consumption:.2f} km/l")
