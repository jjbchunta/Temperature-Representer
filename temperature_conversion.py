import random

# Take a celsius measurement, and convert it to a completely random temperature scale.
def convertCelsiusToRandomScale(celsius):
    scales = {
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15,
        "Réaumur": lambda c: c * 4/5,
        "Rankine": lambda c: (c + 273.15) * 9/5,
        # Placeholder conversion for obscure scales, assuming a fictional linear relationship for demonstration
        # This is a simplification and not accurate for historical or specific scales
        "Obscure": lambda c: c * random.uniform(0.8, 1.2) + random.uniform(-10, 10)
    }

    all_scales = [
        "Amontons", "Barnsdorf", "Beaumuir", "Bénart", "Bergen", "Brisson", "Cimento", "Cruquius", "Dalencé",
        "Daltons", "Daniell", "De la Hire", "De la Ville", "Delisle", "De Luc", "de Revillas", "Derham", "de Suede",
        "de Villeneuve", "Du Crest", "Edinburgh", "Electron Volts", "Fahrenheit", "Florentine", "Florentine Magnum",
        "Fowler", "Frick", "Gas Mark", "Goubert", "Hales", "Hanow", "Hauksbee", "Hoffmann CG", "Jacobs-Holborn",
        "Kelvins", "Kirch", "La Court", "Lambert", "Lange", "Leiden", "Ludolf", "Mariotte", "Miles", "Murray", "Newton",
        "Oertel", "Paris", "Plancks", "Poleni", "Réaumur", "Rømer", "Rankine", "Richter", "Rinaldini", "Rosenthal",
        "Royal Society of London", "Sagredo", "Saint-Patrice", "Stufe", "Sue de Lyon", "Sulzer", "Thermostat",
        "Wedgwood"
    ]

    selected_scale = random.choice(all_scales)
    if selected_scale in scales:
        conversion_formula = scales[selected_scale]
    else:
        conversion_formula = scales["Obscure"]

    converted_temp = round(conversion_formula(celsius))

    return formatConversion({
        "originalTemp": celsius,
        "newTemp": converted_temp,
        "scale": selected_scale
    })

# Take the response from a convertCelsiusToRandomScale call, and format it to a string.
def formatConversion(data):
    originalTemp = data['originalTemp']
    newTemp = data['newTemp']
    scale = data['scale']
    return f"{newTemp} {scale} ({originalTemp}°C)"