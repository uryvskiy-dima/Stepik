#!/usr/bin/env python3

print("Content-type: text/html")
print()
print("<html>")
print("<body>")
print("<table>")
print("<tr>")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"<td>{i * j}</td>")
    print("</tr>")
print("</table>")
print("</body>")
print("</html>")