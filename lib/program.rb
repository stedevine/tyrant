require 'date'

startDate = Date.today

# optionally pass in a start date e.g. Nov or August
for arg in ARGV
   startDate = Date.parse(arg)
end

#puts startDate

tyrants = ["Dave", "Edwin", "Kevin", "Julian", "Ste", "Steve"]

tyrants = tyrants.shuffle


tyrants.each { |t|
puts "%s is tyrant for %s" % [t, startDate.strftime("%B")]
startDate = startDate >> 1
}
