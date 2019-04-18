# ml_final

analogy_mixer.py:
  To be run after we have the two lists of analogies (one created from the original embedding and one created from the debiased embedding)
  This script will randomly mix the lists and write them to non_labeled.txt and labeled.txt. 
  The file labeled.txt will indicate which originial list (biased or debiased) each analogy came from. 
  
After analogy_mixer.py is run and non_labeled.txt is created, go through each analogy in non_labeled.txt and edit the file to indicate 
whether you think the analogy contains a gender bias or is appropriate by typing 'b' or 'a' after the analogy.

  For example, the first line of the file may look like this after you indicate your vote:          hokie-hoo a
  
analogy_counter.py:
  To be run after all analogies have been voted on in non_labeled.txt.
  This script will read labeled.txt and non_labeled.txt to determine the percent of analogies that were voted to contain gender bias
  before debiasing and after debiasing. 
  

  
