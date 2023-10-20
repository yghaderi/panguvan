:py:mod:`panguvan.models.ise`
=============================

.. py:module:: panguvan.models.ise


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   panguvan.models.ise.Date
   panguvan.models.ise.EconomicSector
   panguvan.models.ise.BusinessSector
   panguvan.models.ise.IndustryGroup
   panguvan.models.ise.Industry
   panguvan.models.ise.Activity
   panguvan.models.ise.Market
   panguvan.models.ise.Instrument
   panguvan.models.ise.DailyHistPrice
   panguvan.models.ise.DailyAdjHistPrice



Functions
~~~~~~~~~

.. autoapisummary::

   panguvan.models.ise.create_tables
   panguvan.models.ise.drop_tables



Attributes
~~~~~~~~~~

.. autoapisummary::

   panguvan.models.ise.ISE
   panguvan.models.ise.ise


.. py:data:: ISE

   

.. py:class:: Date(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'date'

      

   .. py:attribute:: date
      :type: datetime.date

      

   .. py:attribute:: jdate
      :type: str

      

   .. py:attribute:: jyear
      :type: int

      

   .. py:attribute:: jmonth
      :type: int

      

   .. py:attribute:: jquarter
      :type: int

      

   .. py:attribute:: jday
      :type: int

      

   .. py:attribute:: jweek_day
      :type: int

      

   .. py:attribute:: jweek_number
      :type: int

      


.. py:class:: EconomicSector(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_economic_sector'

      

   .. py:attribute:: id
      :type: int

      

   .. py:attribute:: name
      :type: str

      


.. py:class:: BusinessSector(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_business_sector'

      

   .. py:attribute:: id
      :type: int

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: economic_sector_id
      :type: int

      


.. py:class:: IndustryGroup(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_industry_group'

      

   .. py:attribute:: id
      :type: int

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: business_sector_id
      :type: int

      


.. py:class:: Industry(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_industry'

      

   .. py:attribute:: id
      :type: int

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: industry_group_id
      :type: int

      


.. py:class:: Activity(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_activity'

      

   .. py:attribute:: id
      :type: int

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: industry_id
      :type: int

      


.. py:class:: Market(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_market'

      

   .. py:attribute:: id
      :type: int

      

   .. py:attribute:: name
      :type: str

      


.. py:class:: Instrument(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_instrument'

      

   .. py:attribute:: ins_id
      :type: str

      

   .. py:attribute:: ins_code
      :type: int

      

   .. py:attribute:: symbol
      :type: str

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: symbol_en
      :type: str

      

   .. py:attribute:: name_en
      :type: str

      

   .. py:attribute:: activity_id
      :type: int

      

   .. py:attribute:: market_id
      :type: int

      


.. py:class:: DailyHistPrice(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_daily_hist_price'

      

   .. py:attribute:: __table_args__
      :value: ()

      

   .. py:attribute:: id
      :type: Optional[int]

      

   .. py:attribute:: date
      :type: datetime.date

      

   .. py:attribute:: ins_id
      :type: str

      

   .. py:attribute:: open
      :type: int

      

   .. py:attribute:: high
      :type: int

      

   .. py:attribute:: low
      :type: int

      

   .. py:attribute:: close
      :type: int

      

   .. py:attribute:: final
      :type: Optional[int]

      

   .. py:attribute:: y_final
      :type: Optional[int]

      

   .. py:attribute:: volume
      :type: int

      

   .. py:attribute:: value
      :type: int

      


.. py:class:: DailyAdjHistPrice(**data: Any)


   Bases: :py:obj:`sqlmodel.SQLModel`

   Usage docs: https://docs.pydantic.dev/2.4/concepts/models/

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of classvars defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The signature for instantiating the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a `RootModel`.

   .. attribute:: __pydantic_serializer__

      The pydantic-core SchemaSerializer used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The pydantic-core SchemaValidator used to validate instances of the model.

   .. attribute:: __pydantic_extra__

      An instance attribute with the values of extra fields from validation when
      `model_config['extra'] == 'allow'`.

   .. attribute:: __pydantic_fields_set__

      An instance attribute with the names of fields explicitly specified during validation.

   .. attribute:: __pydantic_private__

      Instance attribute with the values of private attributes set on the model instance.

   .. py:attribute:: __tablename__
      :value: 'ise_daily_adj_hist_price'

      

   .. py:attribute:: __table_args__
      :value: ()

      

   .. py:attribute:: id
      :type: Optional[int]

      

   .. py:attribute:: date
      :type: datetime.date

      

   .. py:attribute:: ins_id
      :type: str

      

   .. py:attribute:: open
      :type: int

      

   .. py:attribute:: high
      :type: int

      

   .. py:attribute:: low
      :type: int

      

   .. py:attribute:: close
      :type: int

      

   .. py:attribute:: final
      :type: Optional[int]

      

   .. py:attribute:: volume
      :type: int

      

   .. py:attribute:: value
      :type: int

      


.. py:function:: create_tables()


.. py:function:: drop_tables()


.. py:data:: ise

   

