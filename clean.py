import pandas as pd

# ── Load the full dataset ──────────────────────────────
df = pd.read_csv("Social_Media_Advertising.csv")

# ── Filter only Instagram data ─────────────────────────
instagram = df[df["Channel_Used"] == "Instagram"].copy()
print(f"Instagram rows: {len(instagram)}")

# ── Fix Acquisition_Cost — remove $ sign ──────────────
instagram["Acquisition_Cost"] = instagram["Acquisition_Cost"].str.replace("$", "", regex=False).astype(float)

# ── Convert columns to numbers ─────────────────────────
instagram["Conversion_Rate"] = pd.to_numeric(instagram["Conversion_Rate"], errors="coerce")
instagram["Clicks"]          = pd.to_numeric(instagram["Clicks"],          errors="coerce")
instagram["Impressions"]     = pd.to_numeric(instagram["Impressions"],      errors="coerce")
instagram["ROI"]             = pd.to_numeric(instagram["ROI"],              errors="coerce")

# ── Calculate KPIs ─────────────────────────────────────
instagram["CTR"]  = (instagram["Clicks"] / instagram["Impressions"]) * 100
instagram["CPA"]  = instagram["Acquisition_Cost"] / instagram["Conversion_Rate"]
instagram["ROAS"] = instagram["ROI"] / instagram["Acquisition_Cost"]

# ── KPI Summary ────────────────────────────────────────
print("\nAverage KPIs across all Instagram ads:")
print(f"Average CTR:  {instagram['CTR'].mean():.2f}%")
print(f"Average CPA:  ${instagram['CPA'].mean():.2f}")
print(f"Average ROAS: {instagram['ROAS'].mean():.4f}x")

# ── Business Question 1 ────────────────────────────────
print("\n📊 Average ROI by Campaign Goal:")
roi_by_goal = instagram.groupby("Campaign_Goal")["ROI"].mean().sort_values(ascending=False)
print(roi_by_goal)

# ── Business Question 2 ────────────────────────────────
print("\n📊 Average CTR by Target Audience:")
ctr_by_audience = instagram.groupby("Target_Audience")["CTR"].mean().sort_values(ascending=False)
print(ctr_by_audience)

# ── Save clean Instagram CSV ───────────────────────────
instagram.to_csv("instagram_clean.csv", index=False)
print("\n✅ Clean file saved as instagram_clean.csv")