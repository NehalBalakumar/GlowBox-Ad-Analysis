import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load clean Instagram data ──────────────────────────
df = pd.read_csv("instagram_clean.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Day_of_Week"] = df["Date"].dt.day_name()

# ── Set a beautiful style ──────────────────────────────
sns.set_theme(style="darkgrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ══════════════════════════════════════════════════════
# CHART 1 — ROI by Campaign Goal (Bar Chart)
# ══════════════════════════════════════════════════════
roi_goal = df.groupby("Campaign_Goal")["ROI"].mean().sort_values(ascending=False)

plt.figure()
sns.barplot(x=roi_goal.index, y=roi_goal.values, palette="magma")
plt.title("Average ROI by Campaign Goal — GlowBox Instagram Ads", fontsize=14, fontweight="bold")
plt.xlabel("Campaign Goal")
plt.ylabel("Average ROI")
plt.tight_layout()
plt.savefig("chart1_roi_by_goal.png", dpi=150)
plt.close()
print("✅ Chart 1 saved — ROI by Campaign Goal")

# ══════════════════════════════════════════════════════
# CHART 2 — ROI by Target Audience (Bar Chart)
# ══════════════════════════════════════════════════════
roi_audience = df.groupby("Target_Audience")["ROI"].mean().sort_values(ascending=False)

plt.figure()
sns.barplot(x=roi_audience.values, y=roi_audience.index, palette="coolwarm")
plt.title("Average ROI by Target Audience — GlowBox Instagram Ads", fontsize=14, fontweight="bold")
plt.xlabel("Average ROI")
plt.ylabel("Target Audience")
plt.tight_layout()
plt.savefig("chart2_roi_by_audience.png", dpi=150)
plt.close()
print("✅ Chart 2 saved — ROI by Target Audience")

# ══════════════════════════════════════════════════════
# CHART 3 — ROI by Day of Week (Bar Chart)
# ══════════════════════════════════════════════════════
day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
roi_day = df.groupby("Day_of_Week")["ROI"].mean().reindex(day_order)

plt.figure()
sns.barplot(x=roi_day.index, y=roi_day.values, palette="viridis")
plt.title("Average ROI by Day of Week — GlowBox Instagram Ads", fontsize=14, fontweight="bold")
plt.xlabel("Day of Week")
plt.ylabel("Average ROI")
plt.tight_layout()
plt.savefig("chart3_roi_by_day.png", dpi=150)
plt.close()
print("✅ Chart 3 saved — ROI by Day of Week")

# ══════════════════════════════════════════════════════
# CHART 4 — Heatmap: Audience vs Day of Week
# ══════════════════════════════════════════════════════
heatmap_data = df.pivot_table(index="Target_Audience", columns="Day_of_Week", values="ROI", aggfunc="mean")
heatmap_data = heatmap_data[day_order]

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlOrRd", linewidths=0.5)
plt.title("ROI Heatmap — Audience vs Day of Week", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("chart4_heatmap.png", dpi=150)
plt.close()
print("✅ Chart 4 saved — Heatmap")

# ══════════════════════════════════════════════════════
# CHART 5 — ROI by Customer Segment (Bar Chart)
# ══════════════════════════════════════════════════════
roi_segment = df.groupby("Customer_Segment")["ROI"].mean().sort_values(ascending=False)

plt.figure()
sns.barplot(x=roi_segment.index, y=roi_segment.values, palette="Blues_d")
plt.title("Average ROI by Customer Segment — GlowBox Instagram Ads", fontsize=14, fontweight="bold")
plt.xlabel("Customer Segment")
plt.ylabel("Average ROI")
plt.tight_layout()
plt.savefig("chart5_roi_by_segment.png", dpi=150)
plt.close()
print("✅ Chart 5 saved — ROI by Customer Segment")

print("\n🎉 All 5 charts saved successfully!")