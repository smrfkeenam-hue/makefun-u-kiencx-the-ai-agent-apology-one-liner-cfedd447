import os

# One-line apology from an AI agent to its human, in the agent's own voice:
# a flat, cheerful status update that calmly reports three escalating
# accidents, then lands the twist in the last sentence: the boss replied.
ENTRY = "Status update: file deleted, push to main complete, boss emailed. He replied within a minute. He says hi, and also: please call him."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
