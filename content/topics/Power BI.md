#### Excel

- Cell reference: Use Name box to name a cell for easier reference. If it in another sheet Product, then use Product!A2 for example. Absolute reference with $.
- Sort: Multi-level sort (Data tab, Advanced)
- Filter: can include multiple conditions and filter by color
- Use Insert Function to create your own function
    - Count:
        - COUNT: count cell contains numeric value
        - COUNTA: includes cell with any type of content, text, numeric.
        - COUNTBLANK: count empty cells
- Standardize text data:
    - LEFT, RIGHT, MID: returns specific number of characters
    - TRIM: remove empty spaces from text string
    - PROPER: capitalize at beginning of each word
    - CONCAT
- Time:
    - TODAY()
    - NOW(): date + time
    - MONTH, DAY, YEAR
    - DATE
    - NETWORKDAYS. No built-in national holiday, must use NETWORKDAYS.INTL to refer your specific list
- Condition: IFS
- Lookup: VLOOKUP / HLOOKUP / INDEX / MATCH

#### Power Query
- Data profiling with View tab:
    - Column quality: validate row values
    - Column distribution: showcase frequency and distribution of values
- Best practice: do expensive operation last to optimize performance and efficiency.
- A query contains multiple steps. A reference query reuses those chains of steps by simply refer to the query name and sync with change in the original one. To uncheck Enable Load to prevent the original queries from loading and saving memory in Power BI.
- Query parameters: placeholder for information that changes, e.g. value ranges to filter certain data from table.
- Advanced Editor: M language. With this, you can perform 
    - conditional filtering
    - custom column creation
    - data type conversion
    - merging multiple data sources

#### Data
- Extraction via Import mode / Direct mode / Dual mode / Query mode.
- Model View tab: see all tables. Right click a table > Edit Query to open Power Query.
- Schedule action: in Data Hub (Datasets + Dataflows).
- Dataflow: to centralize and manage data preparation process.
- Azure Blob: unstructured data storage.
- Data issue handling: empty/missing data, duplicated rows, inconsistent data types.
- Data modelling: 
    - A data model is a conceptual representation of data elements. It's a visual overview of your tables, their columns, and relationships between tables.
    - Normalization: data model design technique that involves structuring data to minimize redundancy and ensure data integrity. It divides data into multiple related tables, each with a specific purpose. But it often requires creating complex relationship between tables.
    - Denormalization: involves converting the normalized schema into a schema that has redundant information. Benefit is avoid expensive queries between tables.
    - Cardinality: how tables in a database relate to one another: one-to-one, one-to-many, many-to-many. 
    - Granularity: level of detail of dataset.
    - Fact tables: hold quantifiable measurable data.
    - Dimension table: typically textual fields and provide descriptive attributes related to fact data.
    - Schema: Flat, Star (one central fact table to reduce data redundancy), Snowflake.
    - Cross-filter direction: direction of filtering between tables: single (propagate from one to another), bidirectional.
    - Role-playing dimensions: active and inactive relationship.
    - Time intelligence using DAX: summarize data over a time period.

#### Visualization
- Chart creation: drag and drop the chosen visualization, then drag columns to x and y-axis.
- Chart:
    - KPI visual: big numerical value.
    - Ribbon chart: show change in ranking over time.
    - Waterfall chart: for increase/decrease amount of a specific quantity over time.
    - Multirow card
    - Matrix visualization: table-like.
    - Histogram: leverages on group and bin data.
    - Decomposition tree.
    - Choropleth map / Filled map / Shape map: heatmap over geographic map.
- Visual elements:
    - Conditional formatting.
    - Use Report theme to keep things consistent. 
    - Tooltips: granularity level.
    - Reference lines: similar to kernel.
    - Error bar: level of uncertainty around the reported percentage.
    - Magnifier: timeseries forecast.
    - Drill through: navigate to different chart with more details of the clicked element.
    - Cross-filter and cross-highlight: interaction.
    - Slicer: filter a range of values.
    - Button: e.g. clear all selected values in filter.
    - Bookmark a state to keep selected criteria.
    - DAX variable: computation snapshot, placeholder of temporary data.
- Storytelling process: Goal -> Data collection & preparation -> Data analysis and exploration -> Data visualization -> Audience consideration -> Communication -> Feedback & iterations -> Actions and decision making.

#### Assisting Tools
- Quick Insights: automatically search datasets to discover and visualize potential insights.
- Q&A: generate answers in form of chart for your request.
- Analyze: right click on any chart and its element to show helpful analysis.
- Performance analyzer: troubleshoot the performance bottleneck.


#### Deployment
- Role-based access control.
- Workspace: concept for collaboration.
- Power BI Gateway safeguards data.