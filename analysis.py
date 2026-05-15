import pandas as pd

# ── Load the clean Instagram data ──────────────────────
df = pd.read_csv("instagram_clean.csv")
print(f"Loaded {len(df)} Instagram rows\n")

# ── Fix date column ────────────────────────────────────
df["Date"] = pd.to_datetime(df["Date"])
df["Day_of_Week"] = df["Date"].dt.day_name()

# ══════════════════════════════════════════════════════
# ANALYSIS 1 — ROI by Target Audience
# Which audience gives GlowBox the best return?
# ══════════════════════════════════════════════════════
print("📊 ANALYSIS 1 — Average ROI by Target Audience:")
roi_audience = df.groupby("Target_Audience")["ROI"].mean().sort_values(ascending=False)
print(roi_audience)

# ══════════════════════════════════════════════════════
# ANALYSIS 2 — Performance by Day of Week
# Which day should GlowBox run their ads?
# ══════════════════════════════════════════════════════
print("\n📊 ANALYSIS 2 — Average ROI by Day of Week:")
roi_day = df.groupby("Day_of_Week")["ROI"].mean().sort_values(ascending=False)
print(roi_day)

# ══════════════════════════════════════════════════════
# ANALYSIS 3 — Clicks by Day of Week
# Which day gets the most engagement?
# ══════════════════════════════════════════════════════
print("\n📊 ANALYSIS 3 — Average Clicks by Day of Week:")
clicks_day = df.groupby("Day_of_Week")["Clicks"].mean().sort_values(ascending=False)
print(clicks_day)

# ══════════════════════════════════════════════════════
# ANALYSIS 4 — Top 10 Highest ROI Campaigns
# Which exact campaigns performed best?
# ══════════════════════════════════════════════════════
print("\n📊 ANALYSIS 4 — Top 10 Highest ROI Campaigns:")
top10 = df[["Campaign_ID","Campaign_Goal","Target_Audience","ROI","Clicks"]].sort_values("ROI", ascending=False).head(10)
print(top10.to_string())

# ══════════════════════════════════════════════════════
# ANALYSIS 5 — ROI by Customer Segment
# Which customer type is most valuable?
# ══════════════════════════════════════════════════════
print("\n📊 ANALYSIS 5 — Average ROI by Customer Segment:")
roi_segment = df.groupby("Customer_Segment")["ROI"].mean().sort_values(ascending=False)
print(roi_segment)