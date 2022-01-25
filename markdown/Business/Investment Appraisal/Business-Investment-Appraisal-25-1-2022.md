<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>
# Investment Appraisal
## Payback Period

 - Under payback method, an investment project is accepted or rejected on the basis of payback period. 
 - Payback period means the period of time that a project requires to recover the money invested in it. It is mostly expressed in years
 - According to payback method, the project that promises quick recovery of initial investment is considered desirable. If the payback period of a project is shorter than or equal to the management's maximum desired payback period, the project is accepted, otherwise rejected.
	 - For example if a company wants to recoup the cost of a machine within 5 years of purchase, the maximum desired payback period of the company would be 5 years. The purchase of the machine would be desirable if it promises a payback period of 5 years or less.

When net annual cash is even (i.e. same cash flow every period), the payback period of the project can be computed by applying the simple formula

$$PaybackPeriod = \frac{InvestmentRequired}{NetAnnualCashInflow}$$

### Example 

 - The Delta company is planning to ourchase a machine to as machine X. Machine X would cost $25,000 and would have a useful life of 10 years with zero salvage value. The expected annual cash inflow of the machine is $10,000
 - Required, compute payback period of machine X and clonclude whether or not the machine would be purchased in the maximum desired payback period of delta company is 3 years. 
 - Solution:
	 - $$PaybackPeriod = \frac{$25000}{$10000} = 2.5years$$
	- Therefore the machine would be payed since the payback period is less than the 3 year period.


### Comparison

Comparison of two or more alternatives - choosing from several alternative projects: 
 - Where funds are limited and several alternative projects are being considered, the project with the fastest payback period is preferred.


### With Uneven Cash Flow

- When projects generate inconsistent or uneven cash inflow (different cash inflow in different periods), the simple formula cannot be used to compute payback period. In such situations, we need to compute the cumulative cash inflow and then apply the following formula.
- $$PaybackPeriod = YearsBeforeFullRecovery + \frac{UnrecoveredCostAtStartYear}{CashFlowDuringYear}$$
#### Example

An investment of $200,000 is expected to generate the following cash inflows in six years: 
Year 1: $70,000 
Year 2: $60,000 
Year 3: $55,000 
Year 4: $40,000 
Year 5: $30,000 
Year 6: $25,000 

Required: Compute payback period of the investment. Should the investment be made if management wants to recover the initial investment in 3 years or less?

| Year | Cash inflow | Cumulative cash inflow |
| ---- | ----------- | ---------------------- |
| 1    | 70,000      | 70,000                 |
| 2    | 60,000      | 130,000                |
| 3    | 55,000      | **185,000**                |
| 4    | **40,000**      | 225,000      <-- full recovery          | 
| 5    | 30,000      | 255,000                |
| 6    | 25,000      | 280,000                |


$$PaybackPeriod = 3 + \frac{(200,000 - 185,000)}{40000} = 3 + 0.375 = 3.375$$

The payback period is greater than the 3 year initial investment and therefore the project is not desirable.

## Average Rate of Return

 - The term “average rate of return” refers to the percentage rate of return that is expected on an investment or asset from the initial investment cost or average investment over the life of the project.
 - The formula for average rate of return is derived by dividing the average profit by the initial investment and then expressed in terms of percentage.

$$ARR = \frac{AverageAnnualProfit}{InitialInvestment}$$

| Net Profit                                                                                                                                                     | >   | Depreciation                                                                                                                                                          | >   | Initial Investment                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calculate the annual net profit from the investment, which could include revenue minus any annual costs or expenses of implementing the project or investment. | >   | If the investment is a fixed asset such as property, plant, or equipment, subtract any depreciation expense from the annual revenue to achieve the annual net profit. | >   | Divide the annual net profit by the initial cost of the asset, or investment. The result of the calculation will yield a decimal. Multiply the result by 100 to show the percentage return as a whole number. |



### Example 

Suppose the purchase of a new computer system that costs $350,000 is forecast to generate the following net cash flows over the next five years (when it needs to be replaced):

Year 1 $100,000 
Year 2 $130,000 
Year 3 $180,000 
Year 4 $150,000 
Year 5 $100,000 

 - There are several steps to calculate the ARR for this project: 
	 - Total net cash inflow over the five years is $660,000 
	 - Projected profit = $660,000 minus $350,000 (for the initial investment) = $310,000
	 - Average annual profit = $310,000 / 5 years = $62,000 per year 
	 - Hence the ARR = $62,000 / $350,000 = 17.7%

## Net Present Value

Net present value (NPV) is the difference between the present value of cash inflows and the present value of cash outflows over a period of time.

$$NPV = Sum Or Present Values – Cost Of Investment$$

 - Discounting is the reverse of calculating compound interest. A discount factor is used to convert the future net cash flow to its present value today. 
 - As an example, suppose an organisation expects to receive $100,000 in three year’s time whilst today’s interest rate is 5%. What is the present value of $100,000? 
 - From the table, we can see that the discount factor for 5% interest over 3 years is 0.8638. Hence, the present value of the $100,000 received in 3 year’s time is $86,380 
 - The NPV is the sum of all discounted cash flows minus the cost of a particular investment project 
	 - NPV = Sum of present values – Cost of investment

### Example

Suppose that new mechanisation for a firm is estimated to cost $300,000 and should last for five years.

It will cost an estimated $50,000 per annum to maintain but will increase the value of the firm’s output by an estimated $150,000. 

Interest rates are currently 5%. Calculate the NPV on the proposed investment

The net cash flow in each year is simply the total cash inflow minus the total cash outflow, i.e. $150,000 minus $50,000 = $100,000

| Period | Net Cash Flow | Discount Factor | Present Value |
| ------ | ------------- | --------------- | ------------- |
| Year 1 | 100,000       | 0.9524          | 95240         |
| Year 2 | 100,000       | 0.9070          | 90,700        |
| Year 3 | 100,000       | 0.8638          | 86380         |
| Year 4 | 100,000       | 0.8227          | 82270         |
| Year 5 | 100,000       | 0.7835          | 78350              |
| Total  | 500,000       |                 | 432940        |


Add the total present value figures and minus the initial investment cost

$$NPV = $432940 - $300000 = $132940 $$

