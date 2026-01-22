import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'job_title': ['Data Scientist', 'Data Analyst', 'Data Engineer', 'ML Engineer', 'Data Scientist', 'Data Analyst', 'Data Engineer', 'ML Engineer'],
    'experience_level': ['SE', 'MI', 'SE', 'EX', 'EN', 'EN', 'MI', 'SE'],
    'salary_in_usd': [150000, 95000, 140000, 190000, 85000, 70000, 110000, 160000],
    'company_location': ['US', 'GB', 'US', 'DE', 'IN', 'CA', 'US', 'FR']
}

df = pd.DataFrame(data)

salary_by_experience = df.groupby('experience_level')['salary_in_usd'].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=salary_by_experience.index, y=salary_by_experience.values, palette='viridis')
plt.title('Average Data Science Salary by Experience Level (USD)')
plt.xlabel('Experience Level (EN: Entry, MI: Mid, SE: Senior, EX: Executive)')
plt.ylabel('Average Salary ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

top_jobs = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)
print(top_jobs)
