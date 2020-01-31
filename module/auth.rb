module Auth
    module_function()
    def login(id)
        members = ['DDangNon','Non','bloger']
        for member in members do
            if member == id
                return true
            end
        end
        return false
    end
end