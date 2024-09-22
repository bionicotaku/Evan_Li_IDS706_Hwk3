import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    # Read the data from the CSV file
    salaryData = pd.read_csv(file_path)
    columns_to_keep = [
        "work_year",
        "experience_level",
        "job_title",
        "salary_in_usd",
        "remote_ratio",
        "company_size",
    ]
    return salaryData[columns_to_keep]

def calculate_stat(data):
    # Calculate descriptive statistics of the data.
    salaryDataDesc = data.describe()
    return salaryDataDesc

def plot_salary_distribution(data):
    # Plot the distribution of salaries.
    plt.figure(figsize=(10, 6))
    data["salary_in_usd"].hist(bins=50)
    plt.title("Distribution of Salaries")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    
    plt.savefig('output/salary_distribution.png')
    plt.show()
    plt.close()

def plot_job_title_distribution(data):
    # Plot the distribution of top 20 job titles.
    plt.figure(figsize=(12, 6))
    job_title_counts = data['job_title'].value_counts().head(20)
    job_title_counts.plot(kind='bar')
    plt.title('Top 20 Job Titles Distribution')
    plt.xlabel('Job Title')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    plt.savefig('output/job_title_distribution.png')
    plt.show()
    plt.close()
    return job_title_counts

def plot_experience_level_distribution(data):
    # Plot the distribution of experience levels.
    plt.figure(figsize=(8, 6))
    experience_level_counts = data['experience_level'].value_counts()
    experience_level_counts.plot(kind='bar')
    plt.title('Experience Level Distribution')
    plt.xlabel('Experience Level')
    plt.ylabel('Count')
    plt.tight_layout()
    
    plt.savefig('output/experience_level_distribution.png')
    plt.show()
    plt.close()
    return experience_level_counts

def plot_average_salary_by_job(data):
    # Plot average salary for top 15 job titles.
    average_salary_by_job = (data
                             .groupby('job_title')['salary_in_usd']
                             .mean().sort_values(ascending=False))
    top_15_jobs = average_salary_by_job.head(15)
    plt.figure(figsize=(12, 8))
    top_15_jobs.plot(kind='bar')
    plt.title('Average Salary by Job Title (Top 15)', fontsize=16)
    plt.xlabel('Job Title', fontsize=12)
    plt.ylabel('Average Salary (USD)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    for i, v in enumerate(top_15_jobs):
        plt.text(i, v, f'${int(v):,}', ha='center', va='bottom')
        
    plt.savefig('output/average_salary_by_job.png')
    plt.show()
    plt.close()

def plot_salary_vs_experience(data):
    # Plot salary vs experience level.
    experience_map = {
        'EN': 0,  # Entry-level
        'MI': 1,  # Mid-level
        'SE': 2,  # Senior
        'EX': 3   # Executive
    }
    data_copy = data.copy()
    data_copy.loc[:, 'experience_numeric'] = (data_copy['experience_level']
                                              .map(experience_map))
    
    plt.figure(figsize=(12, 8))
    plt.scatter(data_copy['experience_numeric'], data_copy['salary_in_usd'], alpha=0.5)
    plt.title('Relationship between Experience Level and Salary', fontsize=16)
    plt.xlabel('Experience Level', fontsize=12)
    plt.ylabel('Salary (USD)', fontsize=12)
    plt.xticks([0, 1, 2, 3], ['Entry', 'Mid', 'Senior', 'Executive'])
    plt.grid(True, linestyle='--', alpha=0.7)
    
    average_salary = data_copy.groupby('experience_level')['salary_in_usd'].mean()
    for i, exp in enumerate(['EN', 'MI', 'SE', 'EX']):
        avg = average_salary[exp]
        plt.text(i, avg, f'${int(avg):,}', ha='center', va='bottom')
    
    plt.savefig('output/salary_vs_experience.png')
    plt.show()
    plt.close()

def calculate_salary_stats_by_experience(data):
    # Calculate salary statistics by experience level.
    return data.groupby('experience_level').agg({
        'salary_in_usd': ['count', 'mean', 'median', 'min', 'max']
    })