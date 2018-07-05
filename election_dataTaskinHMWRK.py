{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "input_file_csv = os.path.join(\"Desktop\\election_data.csv\")\n",
    "output_result = os.path.join(\".\",\"txt_file\")\n",
    "total_votes = 0\n",
    "count = 0\n",
    "voter_output = \" \"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "# candidates, and votes ###\n",
    "candidates_options = [ ] \n",
    "candidates_votes = dict()\n",
    "winner = \" \"\n",
    "winner_votes = 0\n",
    "total_votes_at_the_poll = 0\n",
    "print (type(candidates_votes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "otes = 0\n",
    "winner_votes = 0\n",
    "total_candidates = 0\n",
    "greatest_votes = [\"\", 0]\n",
    "candidate_options = []\n",
    "candidate_votes = {}\n",
    "\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'file_to_load' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-44-efeb0f1c23cd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfile_to_load\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0melection_data\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m   \u001b[0mreader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcsv\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mDictReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melection_data\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mreader\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m       \u001b[0mvotes\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvotes\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m       \u001b[0mtotal_candidates\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"Candidate\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'file_to_load' is not defined"
     ]
    }
   ],
   "source": [
    "  with open(file_to_load) as election_data:\n",
    "    reader = csv.DictReader(election_data)\n",
    "for row in reader:\n",
    "        votes = votes + 1\n",
    "        total_candidates = row[\"Candidate\"]        \n",
    "\n",
    "        if row[\"Candidate\"] not in candidate_options:\n",
    "            \n",
    "            candidate_options.append(row[\"Candidate\"])\n",
    "\n",
    "            candidate_votes[row[\"Candidate\"]] = 1\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# printing the number of votes here \n",
    "count+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'row' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-46-80f0053b49e6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#print(\". \",end=\"\"),\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mcandidate_name\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'row' is not defined"
     ]
    }
   ],
   "source": [
    "#print(\". \",end=\"\"),\n",
    "candidate_name = row[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "#print (candidates_name)\n",
    "total_votes_at_the_poll+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (<ipython-input-35-db95959c751b>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-35-db95959c751b>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    candidates_options.append(candidates_name)\u001b[0m\n\u001b[1;37m                     ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "# Create the key : Candidate name and value: the number of votes\n",
    "if candidates_name not in candidates_options:\n",
    "candidates_options.append(candidates_name)\n",
    "print (\"list\",candidates_options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-48-1ef771a846ec>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-48-1ef771a846ec>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    else:candidate_votes[row[\"Candidate\"]] = candidate_votes[row[\"Candidate\"]] + 1\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "else:candidate_votes[row[\"Candidate\"]] = candidate_votes[row[\"Candidate\"]] + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-38-98fa0eb964b0>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-38-98fa0eb964b0>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    for candidate in candidates_votes:\u001b[0m\n\u001b[1;37m                                      ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "for candidate in candidates_votes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'candidate' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-49-be4714a741af>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mvotes\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcandidates_votes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcandidate\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'candidate' is not defined"
     ]
    }
   ],
   "source": [
    "votes = candidates_votes.get(candidate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-40-faaae314e431>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-40-faaae314e431>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    vote_percentage = float(votes)/float(total_votes_at_the_poll) * 100\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "#print (\"candidate\",candidate)\n",
    "    #     print (votes)        \n",
    "        vote_percentage = float(votes)/float(total_votes_at_the_poll) * 100\n",
    "        #print (\"vote_percentage\",vote_percentage)\n",
    "        if votes > winner_votes:\n",
    "            winner_votes = votes\n",
    "            winner = candidate\n",
    "         # candidates voter count and percentage\n",
    "        for candidate in candidates_options:\n",
    "            voter_output = voter_output + f\"{candidate}: {vote_percentage:.3f}% ({votes})\\n\"\n",
    "        print (\"voter_output\",voter_output)\n",
    "    #     print(voter_output,end=\"\")\n",
    "        txt_file.write(voter_output)\n",
    "    winning_candidate_summary = (\n",
    "         f\"---------------------\\n\"\n",
    "         f\"Winner: {winner}\\n\"\n",
    "         f\"----------------------\\n\")\n",
    "    \n",
    "    print (winning_candidate_summary)\n",
    "    \n",
    "    txt_file.write(winning_candidate_summary)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Election Results\n"
     ]
    }
   ],
   "source": [
    "print()\n",
    "print(\"Election Results\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Votes 14567554324\n"
     ]
    }
   ],
   "source": [
    "print(\"Total Votes \" + str(14567554324))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'txt_file' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-54-064f075eedc0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mtxt_file\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvoter_output\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'txt_file' is not defined"
     ]
    }
   ],
   "source": [
    "txt_file.write(voter_output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------------------\n",
      "Winner:  \n",
      "----------------------\n",
      "\n"
     ]
    }
   ],
   "source": [
    "winning_candidate_summary = (f\"---------------------\\n\"\n",
    "         f\"Winner: {winner}\\n\"\n",
    "         f\"----------------------\\n\")\n",
    "    \n",
    "print (winning_candidate_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:Anaconda3]",
   "language": "python",
   "name": "conda-env-Anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
