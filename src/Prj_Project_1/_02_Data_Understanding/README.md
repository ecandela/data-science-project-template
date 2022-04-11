## Business Understanding

### - Business Understanding Overview ###

> The data understanding phase of CRISP-DM involves taking a closer look at the data available for mining. This step is critical in avoiding unexpected problems during the next phase--data preparation--which is typically the longest part of a project. Data understanding involves accessing the data and exploring it using tables and graphics that can be organized in IBM® SPSS® Modeler using the CRISP-DM project tool. This enables you to determine the quality of the data and describe the results of these steps in the project documentation.

### - Collecting Initial Data ###

At this point in CRISP-DM, you're ready to access data and bring it into IBM® SPSS® Modeler. Data come from a variety of sources, such as:

Existing data. This includes a wide variety of data, such as transactional data, survey data, Web logs, etc. Consider whether the existing data are enough to meet your needs.
Purchased data. Does your organization use supplemental data, such as demographics? If not, consider whether it may be needed.
Additional data. If the above sources don't meet your needs, you may need to conduct surveys or begin additional tracking to supplement the existing data stores.
Task List

Take a look at the data in IBM SPSS Modeler and consider the following questions. Be sure to take notes on your findings. See the topic Writing a Data Collection Report for more information.

Which attributes (columns) from the database seem most promising?
Which attributes seem irrelevant and can be excluded?
Is there enough data to draw generalizable conclusions or make accurate predictions?
Are there too many attributes for your modeling method of choice?
Are you merging various data sources? If so, are there areas that might pose a problem when merging?
Have you considered how missing values are handled in each of your data sources?

### - Describing Data ###
There are many ways to describe data, but most descriptions focus on the quantity and quality of the data--how much data is available and the condition of the data. Listed below are some key characteristics to address when describing data.

Amount of data. For most modeling techniques, there are trade-offs associated with data size. Large data sets can produce more accurate models, but they can also lengthen the processing time. Consider whether using a subset of data is a possibility. When taking notes for the final report, be sure to include size statistics for all data sets, and remember to consider both the number of records as well as fields (attributes) when describing data.
Value types. Data can take a variety of formats, such as numeric, categorical (string), or Boolean (true/false). Paying attention to value type can head off problems during later modeling.
Coding schemes. Frequently, values in the database are representations of characteristics such as gender or product type. For example, one data set may use M and F to represent male and female, while another may use the numeric values 1 and 2. Note any conflicting schemes in the data report.
With this knowledge in hand, you are now ready to write the data description report and share your findings with a larger audience.

### - Verifying Data Quality ###
Data are rarely perfect. In fact, most data contain coding errors, missing values, or other types of inconsistencies that make analysis tricky at times. One way to avoid potential pitfalls is to conduct a thorough quality analysis of available data before modeling.

The reporting tools in IBM® SPSS® Modeler (such as the Data Audit, Table and other output nodes) can help you look for the following types of problems:

Missing data include values that are blank or coded as a non-response (such as $null$, ?, or 999).
Data errors are usually typographical errors made in entering the data.
Measurement errors include data that are entered correctly but are based on an incorrect measurement scheme.
Coding inconsistencies typically involve nonstandard units of measurement or value inconsistencies, such as the use of both M and male for gender.
Bad metadata include mismatches between the apparent meaning of a field and the meaning stated in a field name or definition..


## Reference
 - IBM Docs. (2021, August 17). Ibm.com. https://www.ibm.com/docs/en/spss-modeler/SaaS?topic=guide-data-understanding -
