# Assignment-4-PLP

## Part 2 - Task 1
### Code Comparison Analysis

After analyzing both implementations, I found significant differences in their design philosophies and performance characteristics. My manual implementation follows a strict validation approach, checking input types and ensuring all dictionaries contain the required key before proceeding. This "fail-fast" methodology catches errors early and provides clear feedback to users about data inconsistencies.

In contrast, the GitHub Copilot code adopts a more permissive strategy, using ".get(key, None)" to handle missing keys gracefully and converting all values to strings. While this prevents crashes, it can produce unexpected sorting results when dealing with mixed data types like numbers and strings.

From a performance perspective, my implementation is more efficient. The lambda function "lambda x: x[key]" directly accesses dictionary keys without additional overhead, whereas Copilot's nested "safe_key" function adds function call costs and unnecessary string conversions for every element during sorting. My upfront validation runs once, while Copilot's safety checks execute repeatedly during the sort operation.

However, Copilot's version offers better fault tolerance for messy, real-world datasets with inconsistent structures. The trade-off is between predictable behavior and flexible handling of imperfect data.

Overall, I believe my implementation strikes the right balance for production use, prioritizing performance and data integrity while maintaining clear error reporting. The strict validation approach ensures consistent, predictable results that are easier to debug and maintain.