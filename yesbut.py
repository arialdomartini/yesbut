import random

excuses = [ "we have no time",
            "we have no budget now",
            "it's not in the roadmap",
            "I need a complete set of UML diagrams for this",
            "we should schedule a meeting to discuss this, first",
            "it's not our business core",
            "we must request a formal approval to the Steering Committee",
            "it's scheduled for the next sprint",
            "you should first open a Jira Ticket with this request",

]

print "...%s" % random.choice(excuses)
