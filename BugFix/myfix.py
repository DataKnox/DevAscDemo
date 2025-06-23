import random

def assign_group(user_id):
    """Randomly assign user to group 'A' or 'B'."""
    random.seed(user_id)  # For reproducibility per user
    return 'A' if random.random() < 0.5 else 'B'

def record_conversion(user_id, converted, results):
    """Record whether a user converted in their assigned group."""
    group = assign_group(user_id)
    if group not in results:
        results[group] = {'total': 0, 'converted': 0}
    results[group]['total'] += 1
    if converted:
        results[group]['converted'] += 1

def report_results(results):
    """Print conversion rates for each group."""
    for group, data in results.items():
        rate = data['converted'] / data['total'] if data['total'] > 0 else 0
        print(f"Group {group}: {data['converted']} / {data['total']} converted ({rate:.2%})")

# Example usage
if __name__ == "__main__":
    results = {}
    # Simulate 1000 users with random conversions
    for user_id in range(1000):
        converted = random.random() < 0.1  # 10% base conversion rate
        record_conversion(user_id, converted, results)
    report_results(results)

