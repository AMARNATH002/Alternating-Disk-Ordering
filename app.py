from flask import Flask, render_template, request

app = Flask(__name__)

# Function to sort the disks using the bubble-swap logic
def solve_disks(n, pattern):
    size = 2 * n

    # Generate initial disk sequence based on pattern
    if pattern == "LD":
        disks = ['L' if i % 2 == 0 else 'D' for i in range(size)]
    else:  # "DL"
        disks = ['D' if i % 2 == 0 else 'L' for i in range(size)]

    initial_disks = disks.copy()
    moves = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(size - 1):
            if disks[i] == 'D' and disks[i + 1] == 'L':
                disks[i], disks[i + 1] = disks[i + 1], disks[i]
                moves += 1
                is_sorted = False

    return initial_disks, disks, moves

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    sorted_disks = []
    moves = 0
    steps = []
    time_complexity = "O(n²) - Bubble sort-like passes through the array"
    initial_disks = []

    if request.method == "POST":
        try:
            n = int(request.form["n"])
            pattern = request.form["pattern"]

            initial_disks, sorted_disks, moves = solve_disks(n, pattern)

            result = f"Sorted Successfully in {moves} moves."
            steps = [
                f"Step 1: Create alternating disks ({' '.join(initial_disks)}).",
                "Step 2: Use bubble-swap where D is before L.",
                "Step 3: Repeat until all Ls are to the left and Ds to the right.",
            ]
        except Exception as e:
            result = f"Error: {str(e)}"

        return render_template("index.html",
                               result=result,
                               moves=moves,
                               sorted_disks=sorted_disks,
                               initial_disks=initial_disks,
                               time_complexity=time_complexity,
                               steps=steps)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
