# Load necessary libraries
library(ggplot2)
library(dplyr)

# Read prediction CSV files for different cell lines and replicates
print("Reading data files...")
a549_1 <- read.csv('./../data/curated/SGNex_A549_directRNA_replicate5_run1_predictions.csv')
a549_2 <- read.csv('./../data/curated/SGNex_A549_directRNA_replicate6_run1_predictions.csv')
hct116_1 <- read.csv('./../data/curated/SGNex_Hct116_directRNA_replicate3_run1_predictions.csv')
hct116_2 <- read.csv('./../data/curated/SGNex_Hct116_directRNA_replicate3_run4_predictions.csv')
hct116_3 <- read.csv('./../data/curated/SGNex_Hct116_directRNA_replicate4_run3_predictions.csv')
hepg2_1 <- read.csv('./../data/curated/SGNex_HepG2_directRNA_replicate5_run2_predictions.csv')
hepg2_2 <- read.csv('./../data/curated/SGNex_HepG2_directRNA_replicate6_run1_predictions.csv')
k562_1 <- read.csv('./../data/curated/SGNex_K562_directRNA_replicate4_run1_predictions.csv')
k562_2 <- read.csv('./../data/curated/SGNex_K562_directRNA_replicate5_run1_predictions.csv')
k562_3 <- read.csv('./../data/curated/SGNex_K562_directRNA_replicate6_run1_predictions.csv')
mcf7_1 <- read.csv('./../data/curated/SGNex_MCF7_directRNA_replicate3_run1_predictions.csv')
mcf7_2 <- read.csv('./../data/curated/SGNex_MCF7_directRNA_replicate4_run1_predictions.csv')
print("Data files read!")

# Rename the 'score' column in each data frame
print("Renaming columns...")
a549_1 <- a549_1 %>% rename(a549_1 = score)
a549_2 <- a549_2 %>% rename(a549_2 = score)
hct116_1 <- hct116_1 %>% rename(hct116_1 = score)
hct116_2 <- hct116_2 %>% rename(hct116_2 = score)
hct116_3 <- hct116_3 %>% rename(hct116_3 = score)
hepg2_1 <- hepg2_1 %>% rename(hepg2_1 = score)
hepg2_2 <- hepg2_2 %>% rename(hepg2_2 = score)
k562_1 <- k562_1 %>% rename(k562_1 = score)
k562_2 <- k562_2 %>% rename(k562_2 = score)
k562_3 <- k562_3 %>% rename(k562_3 = score)
mcf7_1 <- mcf7_1 %>% rename(mcf7_1 = score)
mcf7_2 <- mcf7_2 %>% rename(mcf7_2 = score)
print("Columns renamed!")

# Remove words after the decimal point in the 'transcript_id' column of mcf7_1
print("Preparing all dataframes...")
mcf7_1$transcript_id <- sub("\\..*$", "", mcf7_1$transcript_id)

# Concatenate 'transcript_id' and 'transcript_position' columns into a new column with "|" separator
concatenate_columns <- function(df) {
  df$transcript_id_position <- paste(df$transcript_id, df$transcript_position, sep = "|")
  df <- select(df, -c(transcript_id, transcript_position))
  return(df)
}

a549_1 <- concatenate_columns(a549_1)
a549_2 <- concatenate_columns(a549_2)
hct116_1 <- concatenate_columns(hct116_1)
hct116_2 <- concatenate_columns(hct116_2)
hct116_3 <- concatenate_columns(hct116_3)
hepg2_1 <- concatenate_columns(hepg2_1)
hepg2_2 <- concatenate_columns(hepg2_2)
k562_1 <- concatenate_columns(k562_1)
k562_2 <- concatenate_columns(k562_2)
k562_3 <- concatenate_columns(k562_3)
mcf7_1 <- concatenate_columns(mcf7_1)
mcf7_2 <- concatenate_columns(mcf7_2)

# Combine selected columns into a single data frame
all_transcript_id_positions <- bind_rows(
  a549_1, a549_2, hct116_1, hct116_2, hct116_3, hepg2_1, hepg2_2,
  k562_1, k562_2, k562_3, mcf7_1, mcf7_2
)
print("Dataframes prepared!")

# Get unique values from the combined data frame
print("Getting the unique transcript IDs and positions...")
unique_transcript_id_positions <- unique(all_transcript_id_positions)
pri_key <- data.frame(transcript_id_position = unique_transcript_id_positions)

# Merge data frames with unique values to create a single data frame
# containing all the columns
print("Joining all datasets together...")
pri_key <- merge(pri_key, a549_1, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, a549_2, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, hct116_1, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, hct116_2, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, hct116_3, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, hepg2_1, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, hepg2_2, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, k562_1, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, k562_2, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, k562_3, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, mcf7_1, by='transcript_id_position', all=T)
pri_key <- merge(pri_key, mcf7_2, by='transcript_id_position', all=T)
print("Datasets joined!")

# Calculate row sums
print("Calculating rowwise sums...")
row_sums <- rowSums(pri_key[, -1])

# Combine row sums with the original data frame
pri_key_with_sums <- cbind(pri_key, row_sums)

# Sort the data frame by row sums in descending order
sorted_pri_key <- pri_key_with_sums[order(-row_sums), ]

# Add a binary flag for prediction scores
binary_pri_key <- pri_key %>%
  mutate_at(-1, ~ ifelse(. > 0.5, 1, 0))

# Calculate row sums for the binary data frame
binary_row_sums <- rowSums(binary_pri_key[, -1])
binary_pri_sums <- cbind(binary_pri_key, binary_row_sums)
sorted_binary_key <- binary_pri_sums[order(-binary_row_sums), ]
print("Calculations completed!")

# Filter for rows with row sums equal to 12
print("Filtering for significant transcripts...")
filtered_df <- binary_pri_sums %>%
  filter(binary_row_sums == 12)
print("Filtered!")

# Export the filtered data frame as a CSV file in the current folder
print("Writing result to disk...")
current_dir <- getwd()
filepath <- file.path(current_dir, "fully_mutated.csv")
write.csv(filtered_df, file=filepath, row.names = F)
print(paste("Results written to:", filepath))
