import csv


rows = []

with open("nyc_311_requests.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        rows.append(row)


open_requests = 0
complaint_counts = {}
borough_counts = {}
open_requests_by_borough = {}
closed_requests_by_borough = {}

for row in rows:
    borough = row["borough"]
    complaint_type = row["complaint_type"]
    status = row["resolution_status"]

    if status == "Open":
        open_requests += 1

    if complaint_type not in complaint_counts:
        complaint_counts[complaint_type] = 0
    complaint_counts[complaint_type] += 1

    if borough not in borough_counts:
        borough_counts[borough] = 0
    borough_counts[borough] += 1

    if borough not in open_requests_by_borough:
        open_requests_by_borough[borough] = 0
    if status == "Open":
        open_requests_by_borough[borough] += 1

    if borough not in closed_requests_by_borough:
        closed_requests_by_borough[borough] = 0
    if status == "Closed":
        closed_requests_by_borough[borough] += 1


most_common_complaint = ""
most_common_complaint_count = 0

for complaint_type in complaint_counts:
    count = complaint_counts[complaint_type]

    if count > most_common_complaint_count:
        most_common_complaint = complaint_type
        most_common_complaint_count = count


borough_with_most_open = ""
most_open_count = 0

for borough in open_requests_by_borough:
    count = open_requests_by_borough[borough]

    if count > most_open_count:
        borough_with_most_open = borough
        most_open_count = count


output_lines = []

output_lines.append(f"Open requests: {open_requests}")
output_lines.append("")

output_lines.append(
    f"Most common complaint type: {most_common_complaint} ({most_common_complaint_count} requests)"
)
output_lines.append("")

output_lines.append("Requests per borough:")
for borough in sorted(borough_counts):
    output_lines.append(f"- {borough}: {borough_counts[borough]}")
output_lines.append("")

output_lines.append("Requests by complaint type:")
sorted_complaints = sorted(
    complaint_counts,
    key=lambda complaint_type: complaint_counts[complaint_type],
    reverse=True,
)

for complaint_type in sorted_complaints:
    output_lines.append(f"- {complaint_type}: {complaint_counts[complaint_type]}")
output_lines.append("")

output_lines.append(
    f"Borough with most open requests: {borough_with_most_open} ({most_open_count} open)"
)
output_lines.append("")

output_lines.append("Closure rate by borough:")
for borough in sorted(borough_counts):
    closed_count = closed_requests_by_borough[borough]
    total_count = borough_counts[borough]
    closure_rate = closed_count / total_count * 100

    output_lines.append(f"- {borough}: {closure_rate:.1f}%")
output_lines.append("")

output_lines.append("Top 3 boroughs by total requests:")
top_boroughs = sorted(
    borough_counts,
    key=lambda borough: (-borough_counts[borough], borough),
)

place = 1
for borough in top_boroughs[:3]:
    output_lines.append(f"{place}. {borough} ({borough_counts[borough]} requests)")
    place += 1


with open("output.txt", "w") as file:
    file.write("\n".join(output_lines) + "\n")

print("Output saved to output.txt")
