# Assignment-4-PLP

## Part 2 - Task 1
### Code Comparison Analysis

After analyzing both implementations, I observed notable differences in design philosophy and performance. My manual implementation emphasizes strict validation, checking input types and ensuring all dictionaries contain the required key before sorting. This "fail-fast" approach catches errors early, providing clear feedback about data inconsistencies and preventing unpredictable behavior.

In contrast, the GitHub Copilot code is more permissive, using `.get(key, None)` to handle missing keys and converting all values to strings for comparison. While this prevents crashes with inconsistent data, it can lead to unexpected sorting results, especially when mixing numbers and strings. Copilot’s approach is more tolerant of real-world, messy datasets but may obscure underlying data issues, making debugging more challenging in some cases.

From a performance standpoint, my implementation is more efficient. The lambda function `lambda x: x[key]` accesses dictionary keys directly, minimizing overhead. My upfront validation runs once, while Copilot’s repeated safety checks and string conversions occur for every element during sorting, adding unnecessary computational cost and potentially slowing down the process for large datasets.

Ultimately, the choice is between strict validation for predictable, maintainable code and flexible handling for imperfect data. I believe my approach offers a better balance for production environments, prioritizing performance, data integrity, and clear error reporting, which leads to more consistent and debuggable results overall.