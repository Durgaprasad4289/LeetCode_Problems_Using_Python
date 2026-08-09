# 🚀 30 Days / 60 Problems — Prefix Sum Roadmap

## 🧠 Prefix Sum → Prefix Sum + HashMap → Prefix Sum + Sliding Window

A focused **30-day, 60-problem roadmap** for building Prefix Sum pattern recognition.

**Main goal:** recognize when a subarray/range condition can be represented using prefix information.

---

### ✅ Focused Patterns

- Basic Prefix Sum
- Prefix Sum + HashMap / HashSet / Frequency Map
- Prefix Sum + Modulo / Parity / State
- 2D Prefix Sum + HashMap
- Prefix Sum + Fixed/Variable Sliding Window

### ❌ Excluded

- Dynamic Programming
- Binary Search
- Monotonic Stack
- Monotonic Deque
- Merge Sort / Divide & Conquer

> ⚠️ **Difficulty-ratio note**
> A strict 20% Hard requirement is difficult to satisfy with only the most canonical pure Prefix Sum problems, because many classic Hard Prefix Sum problems depend on techniques explicitly excluded above. Therefore, this roadmap stays within the requested Prefix-centric family and uses one deliberate Hard re-solve instead of sneaking in DP, Binary Search, Stack, or Deque problems.

---

## 🎯 Challenge Statistics

| Difficulty | Count | Percentage |
|:--|--:|--:|
| 🟢 Easy | **12** | **20%** |
| 🟡 Medium | **36** | **60%** |
| 🔴 Hard | **12** | **20%** |
| **Total** | **60** | **100%** |

Daily target: **2 problems × 30 days = 60 practice slots.**

---

## 📅 30-Day Roadmap

### 🗓️ Week 1 — Prefix Sum Fundamentals

| Day | Problem 1 | Difficulty | Pattern | Problem 2 | Difficulty | Pattern |
|:--:|:--|:--:|:--|:--|:--:|:--|
| 1 | [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | 🟢 Easy | Prefix Sum | [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | 🟢 Easy | Prefix Sum |
| 2 | [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | 🟢 Easy | Prefix Sum | [1413. Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) | 🟢 Easy | Prefix Sum |
| 3 | [1732. Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/) | 🟢 Easy | Prefix Sum | [1991. Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/) | 🟢 Easy | Prefix Sum |
| 4 | [2574. Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/) | 🟢 Easy | Prefix Sum | [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/) | 🟢 Easy | Prefix Sum |
| 5 | [1422. Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) | 🟢 Easy | Prefix Sum | [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 🟢 Easy | Prefix Sum + Fixed Window |
| 6 | [2379. Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) | 🟢 Easy | Prefix Sum + Fixed Window | [1652. Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/) | 🟡 Medium | Prefix Sum + Window |
| 7 | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | 🟡 Medium | Prefix + HashMap | [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/) | 🟡 Medium | Prefix + HashMap |

### 🗓️ Week 2 — Prefix Sum + HashMap

| Day | Problem 1 | Difficulty | Pattern | Problem 2 | Difficulty | Pattern |
|:--:|:--|:--:|:--|:--|:--:|:--|
| 8 | [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | 🟡 Medium | Prefix + HashMap + Modulo | [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | 🟡 Medium | Prefix + HashMap + Modulo |
| 9 | [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | 🟡 Medium | Prefix + HashMap | [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | 🟡 Medium | Prefix + HashMap |
| 10 | [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | 🟡 Medium | Prefix + HashMap | [1124. Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/) | 🟡 Medium | Prefix + HashMap |
| 11 | [1546. Maximum Non-Overlapping Subarrays With Sum Equals Target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) | 🟡 Medium | Prefix + HashSet | [1524. Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/) | 🟡 Medium | Prefix + HashMap |
| 12 | [1590. Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/) | 🟡 Medium | Prefix + HashMap + Modulo | [1371. Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/) | 🟡 Medium | Prefix State + HashMap |
| 13 | [1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/) | 🟡 Medium | Prefix State + HashMap | [1983. Widest Pair of Indices With Equal Range Sum](https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/) | 🟡 Medium | Prefix + HashMap |
| 14 | [2488. Count Subarrays With Median K](https://leetcode.com/problems/count-subarrays-with-median-k/) | 🔴 Hard | Prefix Transform + HashMap | [1542. Find Longest Awesome Substring](https://leetcode.com/problems/find-longest-awesome-substring/) | 🔴 Hard | Prefix State + HashMap |

### 🗓️ Week 3 — Prefix Sum Variations + 2D

| Day | Problem 1 | Difficulty | Pattern | Problem 2 | Difficulty | Pattern |
|:--:|:--|:--:|:--|:--|:--:|:--|
| 15 | [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 🟡 Medium | Prefix + Sliding Window | [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | 🟡 Medium | Prefix + Sliding Window |
| 16 | [1052. Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/) | 🟡 Medium | Prefix + Fixed Window | [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | 🟡 Medium | Prefix + Fixed Window |
| 17 | [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | 🟡 Medium | Prefix + Sliding Window | [2090. K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) | 🟡 Medium | Prefix + Fixed Window |
| 18 | [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | 🟡 Medium | Prefix + Sliding Window | [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | 🟡 Medium | Prefix + Fixed Window |
| 19 | [2269. Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | 🟢 Easy | Prefix-style Fixed Window | [1074. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) | 🔴 Hard | 2D Prefix + HashMap |
| 20 | [2302. Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) | 🔴 Hard | Prefix Sum + Sliding Window | [2106. Maximum Fruits Harvested After at Most K Steps](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) | 🔴 Hard | Prefix Sum + Sliding Window |
| 21 | [3445. Maximum Difference Between Even and Odd Frequency II](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/) | 🔴 Hard | Prefix State + Sliding Window | 3729. Count Distinct Subarrays Divisible by K in Sorted Array | 🔴 Hard | Prefix Sum + Hashing |

> Note: problem #3729 above doesn't correspond to a known/verified LeetCode ID as of this roadmap's creation — double-check the number before relying on it, and swap in a verified problem if it doesn't resolve.

### 🗓️ Week 4 — Prefix Sum + Sliding Window

| Day | Problem 1 | Difficulty | Pattern | Problem 2 | Difficulty | Pattern |
|:--:|:--|:--:|:--|:--|:--:|:--|
| 22 | [3347. Maximum Frequency of an Element After Performing Operations II](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) | 🔴 Hard | Prefix Sum + Sliding Window | [2968. Apply Operations to Maximize Frequency Score](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/) | 🔴 Hard | Prefix Sum + Sliding Window |
| 23 | [1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | 🟡 Medium | Prefix Sum + Sliding Window | [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/) | 🟡 Medium | Sliding Window + Prefix Counting |
| 24 | [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) | 🟡 Medium | Sliding Window + Prefix Counting | [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | 🔴 Hard | Sliding Window + Prefix Counting |
| 25 | [2444. Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/) | 🔴 Hard | Sliding Window + Prefix Counting | [1314. Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | 🟡 Medium | 2D Prefix Sum |
| 26 | [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | 🟡 Medium | 2D Prefix Sum | [1685. Sum of Absolute Differences in a Sorted Array](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/) | 🟡 Medium | Prefix Sum |
| 27 | [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) | 🟡 Medium | Prefix Sum | [2025. Maximum Number of Ways to Partition an Array](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) | 🟡 Medium | Prefix Sum + HashMap |
| 28 | [2100. Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) | 🟡 Medium | Prefix Counts | [2483. Minimum Penalty for a Shop](https://leetcode.com/problems/minimum-penalty-for-a-shop/) | 🟡 Medium | Prefix Sum |

### 🗓️ Week 5 — Advanced Prefix-Centric Interview Problems

| Day | Problem 1 | Difficulty | Pattern | Problem 2 | Difficulty | Pattern |
|:--:|:--|:--:|:--|:--|:--:|:--|
| 29 | [2348. Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/) | 🟡 Medium | Prefix Counting | [2155. All Divisions With the Highest Score of a Binary Array](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/) | 🟡 Medium | Prefix Sum |
| 30 | [2640. Find the Score of All Prefixes of an Array](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/) | 🟡 Medium | Prefix Sum + Running Maximum | 1074. Number of Submatrices That Sum to Target — **Final Re-solve** | 🔴 Hard | 2D Prefix + HashMap |

---

## ⭐ The 3 Patterns You MUST Master

### 1️⃣ Basic Prefix Sum

**Recognition** — think Prefix Sum when you see:
- Running cumulative totals
- Repeated range sums
- Left sum vs right sum
- Fixed-range sum queries
- Matrix rectangle sums

**Formula**

```text
prefix[i + 1] = prefix[i] + nums[i]

sum(l, r) = prefix[r + 1] - prefix[l]
```

**Core Problems**
- 1480. Running Sum of 1d Array
- 303. Range Sum Query - Immutable
- 724. Find Pivot Index
- 1732. Find the Highest Altitude
- 1991. Find the Middle Index in Array
- 2574. Left and Right Sum Differences
- 1588. Sum of All Odd Length Subarrays
- 1314. Matrix Block Sum
- 304. Range Sum Query 2D - Immutable

---

### 2️⃣ Prefix Sum + HashMap ⭐⭐⭐

This is the **highest-priority pattern** in the roadmap.

**Core Equation**

```text
prefix[j] - prefix[i] = target
```

therefore:

```text
prefix[i] = prefix[j] - target
```

For counting subarrays:

```python
prefix = 0
count = 0
seen = {0: 1}

for num in nums:
    prefix += num
    count += seen.get(prefix - k, 0)
    seen[prefix] = seen.get(prefix, 0) + 1
```

**Recognition Signals**

| Problem clue | Think |
|:--|:--|
| Subarray sum = K | Prefix + HashMap |
| Count subarrays with sum K | Prefix + Frequency Map |
| Longest subarray with a sum condition | Prefix + HashMap |
| Divisible by K | Prefix + Modulo + HashMap |
| Equal 0s and 1s | Prefix Transform + HashMap |
| Odd/even condition | Prefix Parity + HashMap |
| Character parity/state | Prefix State + HashMap |

**Must-Master Problems**
- 560. Subarray Sum Equals K
- 525. Contiguous Array
- 974. Subarray Sums Divisible by K
- 523. Continuous Subarray Sum
- 930. Binary Subarrays With Sum
- 1248. Count Number of Nice Subarrays
- 325. Maximum Size Subarray Sum Equals k
- 1124. Longest Well-Performing Interval
- 1590. Make Sum Divisible by P
- 1371. Find the Longest Substring Containing Vowels in Even Counts
- 1915. Number of Wonderful Substrings
- 2488. Count Subarrays With Median K
- 1542. Find Longest Awesome Substring

---

### 3️⃣ Prefix Sum + Sliding Window

Use this family when a window's sum can be maintained efficiently.

**Recognition Signals**
- Fixed-size subarray
- Minimum/maximum sum window
- Minimum length satisfying a target
- Positive numbers where the window can expand/shrink safely
- Window sum can be updated incrementally

**Fixed Window**

```text
window_sum = prefix[i + k] - prefix[i]
```

**Core Problems**
- 209. Minimum Size Subarray Sum
- 1658. Minimum Operations to Reduce X to Zero
- 1052. Grumpy Bookstore Owner
- 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
- 1423. Maximum Points You Can Obtain from Cards
- 2090. K Radius Subarray Averages
- 2461. Maximum Sum of Distinct Subarrays With Length K
- 1456. Maximum Number of Vowels in a Substring of Given Length
- 2302. Count Subarrays With Score Less Than K
- 2106. Maximum Fruits Harvested After at Most K Steps
- 3445. Maximum Difference Between Even and Odd Frequency II

---

## 🧠 Prefix Sum Recognition Cheat Sheet

| If the problem says... | Think... |
|:--|:--|
| Running cumulative total | Prefix Sum |
| Repeated range sum | Prefix Sum |
| Left sum vs right sum | Prefix Sum |
| Subarray sum = K | Prefix + HashMap |
| Count subarrays with sum K | Prefix + Frequency Map |
| Longest subarray with sum K | Prefix + HashMap |
| Divisible by K | Prefix + Modulo + HashMap |
| Equal number of 0s and 1s | Prefix Transform + HashMap |
| Odd/even subarray condition | Prefix Parity + HashMap |
| Character parity/state | Prefix State + HashMap |
| Matrix rectangle sum | 2D Prefix Sum |
| Submatrices sum to target | 2D Prefix + HashMap |
| Fixed-size window sum | Prefix + Sliding Window |
| Minimum subarray sum with positive numbers | Sliding Window / Prefix Sum |

---

## 🔥 Tier 1 — MUST SOLVE

If you cannot finish all 60, prioritize these first:

1. 560. Subarray Sum Equals K
2. 525. Contiguous Array
3. 974. Subarray Sums Divisible by K
4. 523. Continuous Subarray Sum
5. 930. Binary Subarrays With Sum
6. 1248. Count Number of Nice Subarrays
7. 325. Maximum Size Subarray Sum Equals k
8. 1124. Longest Well-Performing Interval
9. 1590. Make Sum Divisible by P
10. 209. Minimum Size Subarray Sum
11. 1658. Minimum Operations to Reduce X to Zero
12. 1074. Number of Submatrices That Sum to Target
13. 2302. Count Subarrays With Score Less Than K
14. 2106. Maximum Fruits Harvested After at Most K Steps

---

## 📝 Daily Practice Method

For each of the 2 daily problems:

### Step 1 — Identify the pattern

Before coding, ask:

```text
1. Is this about a contiguous subarray/range?
2. Is there a sum relationship?
3. Can the subarray be expressed using two prefix sums?
4. Do I need previous prefix states?
5. Should a HashMap store those states?
6. Can a sliding window maintain the condition?
```

### Step 2 — Write the brute-force idea

```text
Brute Force
O(n²)
```

Then ask: *what repeated calculation can Prefix Sum remove?*

### Step 3 — Derive the optimized pattern

```text
Brute Force
    ↓
Prefix Sum
    ↓
Prefix + HashMap
       OR
Prefix + Sliding Window
```

### Step 4 — Code

Only code after you can explain why the pattern works.

### Step 5 — Re-solve

At the beginning of each study session, spend 10–15 minutes re-solving one previous problem without looking at your old code.

---

## 🏆 Final Goal

When you see:

> "Find the number of continuous subarrays whose sum equals K."

your thought process should become:

```text
Subarray
   ↓
Sum relationship
   ↓
Prefix Sum
   ↓
Need previous prefix?
   ↓
HashMap
   ↓
O(n)
```

For a positive-number minimum-sum problem:

```text
Subarray
   ↓
Positive numbers
   ↓
Sum condition
   ↓
Sliding Window
```

**🚀 Master the pattern, not the problem.**