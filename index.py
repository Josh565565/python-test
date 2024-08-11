from bs4 import BeautifulSoup

html_content = """
<html>
  <head>
    <title>Our Python Class exam</title>

    <style type="text/css">
      body {
        width: 1000px;
        margin: auto;
      }
      table,
      tr,
      td {
        border: solid;
        padding: 5px;
      }
      table {
        border-collapse: collapse;
        width: 100%;
      }
      h3 {
        font-size: 25px;
        color: green;
        text-align: center;
        margin-top: 100px;
      }
      p {
        font-size: 18px;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <h3>
      TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK
    </h3>
    <table>
      <thead>
        <th>DAY</th>
        <th>COLOURS</th>
      </thead>
      <tbody>
        <tr>
          <td>MONDAY</td>
          <td>
            GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE,
            CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
          </td>
        </tr>
        <tr>
          <td>TUESDAY</td>
          <td>
            ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE,
            ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE
          </td>
        </tr>
        <tr>
          <td>WEDNESDAY</td>
          <td>
            GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED,
            ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE
          </td>
        </tr>
        <tr>
          <td>THURSDAY</td>
          <td>
            BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM,
            ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
          </td>
        </tr>
        <tr>
          <td>FRIDAY</td>
          <td>
            GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED,
            RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE
          </td>
        </tr>
      </tbody>
    </table>

    <p>
      Examine the sequence below very well, you will discover that for every 1s
      that appear 3 times, the output will be one, otherwise the output will be
      0.
    </p>
    <p>
      0101101011101011011101101000111 <span style="color: orange">Input</span>
    </p>
    <p>
      0000000000100000000100000000001 <span style="color: orange">Output</span>
    </p>
    <p></p>
  </body>
</html>

"""

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table')

# Extract data from table rows
data = []
for row in table.find_all('tr')[1:]:
    day, colors_str = [cell.text for cell in row.find_all('td')]
    colors = [color.strip() for color in colors_str.split(',')]
    data.extend(colors)


from collections import Counter
import statistics

color_counts = Counter(data)

# 1. Mean Color
mean_color = color_counts.most_common(1)[0][0]

# 2. Mostly Worn Color
most_worn_color = color_counts.most_common(1)[0][0]

# 3. Median Color
sorted_colors = sorted(data)
median_color = sorted_colors[len(sorted_colors) // 2]

# 4. Variance of Colors
color_mapping = {color: i for i, color in enumerate(set(data))}
numeric_data = [color_mapping[color] for color in data]
variance = statistics.variance(numeric_data)

# 5. Probability of Red
prob_red = color_counts['RED'] / len(data)

print("1. Mean Color:", mean_color)
print("2. Mostly Worn Color:", most_worn_color)
print("3. Median Color:", median_color)
print("4. Variance of Colors:", variance)
print("5. Probability of Red:", prob_red)


import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


# Established connection to PostgreSQL database
conn = psycopg2.connect(
    dbname=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_PORT'),
)
cur = conn.cursor()

# Create DB table
cur.execute('''
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(255) PRIMARY KEY,
        frequency INTEGER
    )
''')

# Add color frequencies to DB
for color, frequency in color_counts.items():
    cur.execute('''
        INSERT INTO color_frequencies (color, frequency)
        VALUES (%s, %s)
        ON CONFLICT (color) DO UPDATE SET frequency = excluded.frequency
    ''', (color, frequency))

conn.commit()
cur.close()
conn.close()


def recursive_search(numbers, target):
    if not numbers:
        return False
    elif numbers[0] == target:
        return True
    else:
        return recursive_search(numbers[1:], target)

numbers = [1, 3, 5, 7, 9]
target = 5
found = recursive_search(numbers, target)
print("Target found:", found)


import random

def generate_binary_to_decimal():
    binary_str = ''.join(random.choice('01') for _ in range(4))
    decimal_num = int(binary_str, 2)
    return binary_str, decimal_num

binary_str, decimal_num = generate_binary_to_decimal()
print("Binary:", binary_str, "Decimal:", decimal_num)


def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        total = a + b
        for _ in range(2, n):
            a, b = b, a + b
            total += b
        return total

sum_50_fibonacci = fibonacci_sum(50)
print("Sum of first 50 Fibonacci numbers:", sum_50_fibonacci)
