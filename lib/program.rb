require 'date'

tyrants = ["Dave", "Edwin", "Phil", "Kevin", "Julian", "Ste", "Steve"]

tyrants = tyrants.shuffle

mydate = Date.today

tyrants.each { |t| 
puts "%s is tyrant for %s" % [t, mydate.strftime("%B")]
mydate = mydate >> 1
}