import pandas as pd
import glob

files = glob.glob("C:/Users/labaz/Desktop/Faks/2. letnik/2. semester/PR/Projekt/Podatki/*.csv")

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

cols = ["surface", "winner_rank", "loser_rank", "winner_age", "loser_age", "w_ace", "l_ace", "w_df", "l_df"]

df = df[cols]

df = df.dropna()

df_rev = df.copy().rename(columns={
    "winner_rank": "loser_rank",
    "loser_rank": "winner_rank",
    "winner_age": "loser_age",
    "loser_age": "winner_age",
    "w_ace": "l_ace",
    "l_ace": "w_ace",
    "w_df": "l_df",
    "l_df": "w_df"
})

df["target"] = 1
df_rev["target"] = 0

df_final = pd.concat([df, df_rev], ignore_index=True)

df_final["rank_diff"] = df_final["winner_rank"] - df_final["loser_rank"]
df_final["age_diff"] = df_final["winner_age"] - df_final["loser_age"]
df_final["ace_diff"] = df_final["w_ace"] - df_final["l_ace"]
df_final["df_diff"] = df_final["w_df"] - df_final["l_df"]

df_final["age_diff_abs"] = abs(df_final["age_diff"])

df_final = df_final[
    ["surface", "rank_diff", "age_diff", "age_diff_abs", "ace_diff", "df_diff", "target"]
]

df_final = pd.get_dummies(df_final, columns=["surface"])

df_final.to_csv("tennis_ml_ready.csv", index=False)

print(df_final.head())
print(df_final.shape)